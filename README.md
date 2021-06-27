## Docker_Compose_File ##



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


