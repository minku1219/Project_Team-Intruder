## Docker_Compose_File for Container Creation ##



```
version: "3.8"
services: 
    minkuapp1:
        image: ubuntu
        container_name: minku1
        command: sleep 500
    minkuapp2:
        image: alpine
        container_name: minku2
        command: ping google.com
    minkuapp3:
        image: alpine
        container_name: minku3
        command: ping google.com

# docker run -itd --name minku1 alpine ping google.com
```



## Docker-Compose Commands



```
docker-compose up -d
docker-compose stop 
docker-compose start
docker-compose down
docker-compose images
docker-compose ps 
```



## Docker_Compose_File for image and conatiner creation using own DockerFile



```
version: "3.8"
services: 
    minkuv1:
        image: minkum:v2
        build: .
        container_name: mk1
        # command: echo Hello World
 ```
 
 
 
