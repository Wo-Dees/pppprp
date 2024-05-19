#!/bin/bash

cd server
docker build -t time-server .
cd ..

cd client
docker build -t time-client .
cd ..

kubectl apply -f server/server.yaml
kubectl apply -f client/client.yaml

kubectl wait --for=condition=available deployment/time-client --timeout=300s

kubectl port-forward service/time-server-service 8888:8888
