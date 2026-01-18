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
