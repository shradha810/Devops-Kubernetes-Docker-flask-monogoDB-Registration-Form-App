# Docker-flask-monogoDB-Registration-Form-App
Built a Flask web application with MongoDB database integration, leveraging the power of Docker Compose.
The application Flask-MongoDB-Application is divided into frontend and backend.
Frontend has the HTML part and backend talks to the database for insertion/querying.

To run the application,
1) edit the variable MONGO in docker-compose.yaml (https://cloud.mongodb.com/ -> database -> ShradhaLearn cluster -> connect) 
You can see all the documents in the collections: https://cloud.mongodb.com/ -> database -> ShradhaLearn cluster -> Collections
2) docker-compose up

![image](https://github.com/shradha810/Docker-flask-monogoDB-Registration-Form-App/assets/60320258/08d1ea8d-3948-4250-b076-f8605a316145)


# Part - 2
I have also established the above Flask-based application using AWS services, specifically Amazon Elastic Container Registry (ECR), Amazon Elastic Container Service (ECS) with AWS Fargate.

ECR Setup:
Two repositories were created in Amazon ECR, namely flask-backend and flask-frontend. Docker images were pushed to these repositories, containing the backend and frontend components of the Flask application.
![image](https://github.com/shradha810/Docker-flask-monogoDB-Registration-Form-App/assets/60320258/19ceee80-1e65-43c6-9dd7-26f9d31d7c13)


ECS Cluster Creation:
A new ECS cluster named flask-application was created with default networking settings.
The infrastructure was set to use AWS Fargate, providing serverless container management.
![image](https://github.com/shradha810/Docker-flask-monogoDB-Registration-Form-App/assets/60320258/94514b80-03b4-428a-ae72-3f8efff3ef37)


Task Definition:
A task definition named flask-application was defined, specifying the containers and their configurations.
Task Execution Role: Configured to enable ECS access to the ECR repository

Container 1 (Backend):
Name: backend
Image URI: Obtained from the flask-backend ECR repository
Port Mapping: Container port 8500, TCP, with the application protocol set to HTTP
Environment: AWS Fargate

Container 2 (Frontend):
Name: frontend
Image URI: Obtained from the flask-frontend ECR repository
Port Mapping: Container port 8000, TCP
Environment Variable: BACKEND_URL set to http://localhost:8500
Environment: AWS Fargate
![image](https://github.com/shradha810/Docker-flask-monogoDB-Registration-Form-App/assets/60320258/506bdf22-cb6c-4d61-951a-5223f2c1cf26)


Service Creation:
A service named application-service was established as an ECS application type (replica). The task definition family flask-application with revision 1 (latest) was associated with this service. The service was configured to maintain one desired task, ensuring a single running instance of the application.
![image](https://github.com/shradha810/Docker-flask-monogoDB-Registration-Form-App/assets/60320258/d7159705-f5f2-4d65-abc2-046b0f1a391f)

![image](https://github.com/shradha810/Docker-flask-monogoDB-Registration-Form-App/assets/60320258/bc1217da-9119-46f7-a789-88f9578a18ef)

