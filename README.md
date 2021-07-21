## Connecting File With Running Container



```
docker run -itd --name webUi -p 6969:80 -v /home/codewars/Devops_Project/webPortal:/var/www/html -v /home/codewars/Devops_Project/webBackend:/var/www/cgi-bin/ 9756004011/httpdimg_new:v1
```


