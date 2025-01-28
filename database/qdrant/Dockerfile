# Stage 1: Build Qdrant from source
FROM rust:1.70 as builder

WORKDIR /qdrant

# Install build dependencies
RUN apt-get update && apt-get install -y \
    clang \
    cmake \
    libssl-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy Qdrant source code (replace '.' with the actual Qdrant source directory)
COPY . .

# Build Qdrant release binary
RUN cargo build --release

# Stage 2: Minimal runtime
FROM debian:bullseye-slim

ENV QDRANT__STORAGE__PATH=/qdrant/storage \
    QDRANT__SERVICE__GRPC_PORT=6334 \
    QDRANT__SERVICE__HTTP_PORT=6333 \
    PATH="/usr/local/bin:$PATH"

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    libssl-dev \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /qdrant

# Copy the built binary from the builder stage
COPY --from=builder /qdrant/target/release/qdrant /usr/local/bin/qdrant

# Create storage directory
RUN mkdir -p /qdrant/storage

# Expose Qdrant ports
EXPOSE 6333 6334

# Start Qdrant
CMD ["qdrant"]
