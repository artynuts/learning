# DOCKER

```
winget install Docker.DockerDesktop
```

Restart the computer
Go through first run
Update wsl is error
```
wsl --update
```

Ensure that docker is installed properly
```
docker --version
```

Check if docker is installed properly
```
docker run hello-world
```

### Adding docker to your project
```
mkdir docker
mkdir docker\postgresql
mkdir docker\postgresql\data
```
> Add docker-compose.yml file

```
cd docker
docker-compose -up -d
```

