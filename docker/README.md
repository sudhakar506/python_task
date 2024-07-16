## Multi-container app using Docker Compose
This sample shows how Docker Compose can be used for multi container app. 
Two containers include 
    1) Sprintboot based business logic 
    2) Postgres DB

### Local deployment
- To compose docker
  - change directory to docker compose
  - ./docker-compose
  - chmod +x ./docker-compose
  - docker-compose --version

### Docker compose deployment
- Database setup
  - Access postgres using local pgadmin
    - Host: public ip of ec2
    - Port: 5432
    - User: admin
    - Password:abc123

### Test Docker Application
- Test application: http://localhost:8080/data/