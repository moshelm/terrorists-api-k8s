משה אלמליח 
322534348
כיתת נגב

# for using in docker 

##  run the app
* option a: create image and container using Dockerfile 
* option b: run localy "python main.py"
##  run container of mongodb 
run :
**docker run -d --name mongo-con -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=secretpass mongo:7.0**


## run docker compose 

* run "docker compose up -d"

# for using k8s

## local using minikube
* **run**: minikube start
* kubectl apply -f k8s
* minikube service svc threat-api-svc

# for using openshift
* login use oc token
* **run** oc apply -f k8s
* oc expose svc threat-api-svc
* oc get route threat-api-svc
* open in brower address in HOST/PORT (sometime you need to remove 's' from https)

# env variabel
MONGO_HOST 
MONGO_PORT 
MONGO_USERNAME
MONNGO_PASSWORD
MONGO_DB
MONGO_AUTH_SOURCE


