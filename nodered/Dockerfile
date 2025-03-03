FROM nodered/node-red
USER root
RUN cd /data && npm install node-red-node-redis && npm install node-red-contrib-redis
USER node-red
