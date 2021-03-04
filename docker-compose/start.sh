docker-compose up -d
sleep 5
kubectl --server=127.0.0.1:8080 apply -f flux-system.yaml
kubectl --server=127.0.0.1:8080 apply -f controller/crd.yaml
docker-compose logs -f
