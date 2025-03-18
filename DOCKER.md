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
### Check if the container is running properly

```
docker ps | findstr postgres
```

### Test the connection

```
docker exec -it postgres_db psql -U postgres -d ai_model_comparison -c "\l"
```

List of databases  
---------------------+----------+----------+-----------------+------------+------------+------------+-----------+-----------------------  
        Name         |  Owner   | Encoding | Locale Provider |  Collate   |   Ctype    | ICU Locale | ICU Rules |   Access privileges   
---------------------+----------+----------+-----------------+------------+------------+------------+-----------+-----------------------  
 ai_model_comparison | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 postgres            | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 template0           | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =c/postgres          +
                     |          |          |                 |            |            |            |           | postgres=CTc/postgres
 template1           | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =c/postgres          +
                     |          |          |                 |            |            |            |           | postgres=CTc/postgres

```
docker exec -it postgres_db psql "postgresql://postgres:postgres@localhost:5432/ai_model_comparison" -c "\conninfo"
```
> You are connected to database "ai_model_comparison" as user "postgres" on host "localhost" (address "::1") at port "5432".

### View the contents of postgresql db


### Backup the content of the database

```
docker exec -t postgres_db pg_dump -U postgres ai_model_comparison > backup_$(Get-Date -Format "yyyyMMdd_HHmmss").sql
```
