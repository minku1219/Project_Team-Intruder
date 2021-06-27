## Connecting Python to Docker Using SDK



```
import docker
client = docker.from_env()
container = client.images.pull("ubuntu")
print(container.id)
```



## ScreenShot ##



<img src="Docker_SDK.png">


