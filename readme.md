# Ironclad Demo Readme

## Project Requirements

1. Create a Web Application with following inputs as mentioned below
   1. First Name , Middle Name & Last Name [ Only strings are allowed. ]
   2. Email Address [ Should be able to detect wrong format on email address]
   3. Phone Number [ Valid USA number format ]
   4. Date of Birth. [ Date should be of the format MM/DD/YYYY only ]
2. Above Inputs should be persisted in a database ( MySQL / Postgres ) and should support CRUD Operations ○ Reading back the contents from the database, it’s ok to return all the records in a text area / table on the application.
   1. For Updating / Deleting the data , you can select the data from the same text area / table where you return all the content.
3. Application & backends should be containerized , exposed as a service and deployed on a K8s / Docker Compose/ Nomad Cluster.

## References

1. [Minikube](https://minikube.sigs.k8s.io/docs/start/)
2. [Postgres](https://hub.docker.com/_/postgres)
3. [MySQL](https://hub.docker.com/_/mysql)
4. [Web Application](https://flask.palletsprojects.com/en/stable/) Language Framework
    of your [own choice](https://www.djangoproject.com/).
5. [k8s](https://kubernetes.io/docs/home/)
6. [compose](https://docs.docker.com/compose/)
7. [nomad](https://www.nomadproject.io/)
