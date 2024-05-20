#  Property management space

This project provides a foundational set of APIs of building a web application that manages properties and its details. It offers core functionalities to create, retrieve, and update property information
## Prerequisites to run the app locally

- Docker Desktop 
-  Python

For, the project I have gone with hosting the MongoDB in a container and the GUI on an another container rather locally so to run the project we need Docker.
## Installation

Clone the Repo

```bash
https://github.com/Gl1tchk0ng/realestateapifm.git
```
Open up the file where you have cloned the Repo and run the following commands in the terminal

```bash
docker compose up --build
```
This command builds up the docker compose file that has 2 containers 
-  mongo &#8594; this container holds the DB 
-  mongo-express &#8594; this contianer is holds the web GUI of the mongoDB that is created above 

Now, we need to copy the data files into the mongo container so that we can load them into a database collection so that we can perform the CRUD applications on it and for that use the following command to copy the files into the docker container for that we need to know what our "mongo" container is Id'd as so run the following command and copy the container Id

```bash
docker ps -a 
```

we now know our container_id by simply running the following cmd and as the next step load the csv files using the below commands

```bash
docker cp <file_location> <container_id>:/properties.csv
```
Now, we have the file inside the docker container the next step is to load it into a DB and to work with the mongo internface we need to open the mongo shell and then load the csv files into a DB so copy the below commands  

```bash
docker exec -it tuio-mongo-1 mongosh -u root -p example --authenticationDatabase admin
```
Just for the simplicity of the project I have set the user name and passcode for the mongo as simple terms feel free to change them to you.

Now we need to load the copied CSV file as a DB we need to run the following command  
```bash
mongoimport --db your_database_name --collection properties --type csv --headerline --file /path/to/yourfile.csv
```
and with that we have our database set to work with 


## Demo

[Demonstration of the API's build for the project](https://drive.google.com/file/d/1IYCBXJWJytAa95Txy9_29FujNNMdKI6_/view?usp=sharing).



## Features

- Create new Porperty for it to be in the database
- Fetch all the properties based on the city
- Update an existing record of a property based on the id 
- Find all cities in the database based on state
- Find similar properties based on the property_id this fucntion searches for properties of the same city and state 

