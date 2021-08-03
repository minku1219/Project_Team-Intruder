## Installation of Jenkins



```
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > \
    /etc/apt/sources.list.d/jenkins.list'
sudo apt-get update
sudo apt install openjdk-11-jdk
java --version
sudo apt-get install jenkins
systemctl status jenkins.service
```

To go to Jenkins Page 

IP:Port (Port is Mostly 8080)
ex- 192.168.68.9:8080
