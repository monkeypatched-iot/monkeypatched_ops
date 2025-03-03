import redis
import numpy as np
import json
from redis.commands.search.query import Query

# Initialize Redis connection
r = redis.Redis(host='localhost', port=6379, db=0)

# Function to create the vector index
def create_vector_index():
    try:
        # Check if the index already exists
        existing_indexes = r.execute_command("FT._LIST")
        if 'idx:bikes_vss' in existing_indexes:
            print("Index already exists!")
            return
        
        r.execute_command(
            'FT.CREATE', 'idx:bikes_vss', 'ON', 'JSON', 'PREFIX', '1', 'bikes:',
            'SCHEMA',
            '$.model', 'TEXT', 'WEIGHT', '1.0', 'NOSTEM',
            '$.brand', 'TEXT', 'WEIGHT', '1.0', 'NOSTEM',
            '$.price', 'NUMERIC',
            '$.type', 'TAG', 'SEPARATOR', ',',
            '$.description', 'TEXT', 'WEIGHT', '1.0',
            '$.description_embeddings', 'AS', 'vector', 'VECTOR', 'FLAT', '6', 
            'TYPE', 'FLOAT32', 'DIM', '768', 'DISTANCE_METRIC', 'COSINE'
        )
        print("Index created successfully!")
    except redis.exceptions.ResponseError as e:
        print(f"Error creating index: {e}")

# Example document with embedding and other fields
def store_document(doc_id, model, brand, price, type_tag, description, embedding):
    doc = {
        'model': model,
        'brand': brand,
        'price': price,
        'type': type_tag,
        'description': description,
        'description_embeddings': embedding.tolist()  # Convert numpy array to list
    }
    # Store document as JSON
    r.json().set(f'bikes:{doc_id}', '$', doc)
    print(f"Document {doc_id} stored successfully!")

def document_to_json(doc):
    doc_dict = {
        "id": doc.id,
        "vector_score": doc.vector_score,
        "model": doc["$.model"],
        "brand": doc["$.brand"],
        "description": doc["$.description"]
    }
    return json.dumps(doc_dict, indent=4)

# Create the vector index
create_vector_index()

# Example document with a 768-dimensional vector embedding (e.g., from a model)
doc1_embedding = np.random.rand(768).astype(np.float32)
doc2_embedding = np.random.rand(768).astype(np.float32)


# Define the query vector (replace with your own vector values)
query_vector = np.random.rand(768).astype(np.float32).tobytes()

# Create the KNN query
query = (
    Query("(*)=>[KNN 3 @vector $query_vector AS vector_score]")
    .sort_by("vector_score")
    .return_fields("vector_score", "$.model", "$.brand", "$.description")
    .dialect(2)  # Use Redis dialect version 2
)

# Execute the query
params = {"query_vector": query_vector}  # Pass vector bytes directly
results = r.ft("idx:bikes_vss").search(query, query_params=params)

# Print results
# Convert each result to JSON

# Store example documents with embeddings
store_document(1, "Mountain Bike", "BrandA", 500, "Mountain, Offroad", "A durable mountain bike", doc1_embedding)
store_document(2, "Road Bike", "BrandB", 700, "Road, Racing", "A fast road bike", doc2_embedding)

for result in results.docs:
    json_doc = document_to_json(result)
    print(json_doc)