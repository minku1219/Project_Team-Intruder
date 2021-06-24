import docker
client = docker.from_env()
container = client.images.pull("ubuntu")
print(container.id)