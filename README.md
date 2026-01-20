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

# create by openshift 
## run this commands

* **creating mongo bc! about name and env**

* oc new-app docker.io/library/mongo:7 --name=mongo -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=secretpass -e MONGO_INITDB_DATABASE=threat_db

* **creating app bc! MONGO_HOST have to be same as --name in mongo**

* oc new-app https://github.com/moshelm/terrorists-api-k8s.git --name=threat-api -e MONGO_HOST=mongo -e MONGO_PORT=27017 -e MONGO_USERNAME=admin -e MONGO_PASSWORD=secretpass -e MONGO_DB=threat_db -e MONGO_AUTH_SOURCE=admin

* oc expose svc threat-api-svc
* oc get route threat-api-svc
* open in brower address in HOST/PORT (sometime you need to remove 's' from https)

# env variabel
1. MONGO_HOST 
2. MONGO_PORT 
3. MONGO_USERNAME
4. MONNGO_PASSWORD
5. MONGO_DB
6. MONGO_AUTH_SOURCE

# to see in mongo compase
* run
* **creating tannel**
* oc port-forward deployment/mongo 27017:27017

* in compase enter this for connection
* mongodb://admin:secretpass@localhost:27017/threat_db?authSource=admin


