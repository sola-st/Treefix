# Extracted from https://stackoverflow.com/questions/44785585/how-can-i-delete-all-local-docker-images
docker rmi $(docker images -a -q)

docker system prune

