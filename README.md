# Project 6: Brevet time calculator service


## What?

An ACPbrevet control time calculator that includes a RESTful API for getting data from the database, either in json or csv format. Based on the calculator: https://rusa.org/octime_acp.html and rules: https://rusa.org/octime_alg.html , https://rusa.org/pages/rulesForRiders . This is a webserver that runs in docker-compose and uses flask, ajax, and mongodb (pymongo).


## Rules

Times follow the table linked in .../octime_alg.html above. Based on the min and max speeds, and the distance from the start to the control, the open and close times for each control are calculated. Only the part of the distance within a threshold follows that min/max speed (e.g. a control at 300km has the first 200km treated as 0-200 and the last 100km treated as 200-400). The time for the final control is based on the given brevet distance, and the final control can be no more that 20% longer than the given brevet distance.


## Functionality

This project has three parts (use the port for the api): 

* A RESTful service to expose what is stored in MongoDB using the following:

   "http://<host:port>/listAll" should return all open and close times in the database
   
   "http://<host:port>/listOpenOnly" should return open times only
   
   "http://<host:port>/listCloseOnly" should return close times only

* Two different representations: one in csv and one in json. For the above, JSON is be is default representation. 

   "http://<host:port>/listAll/csv" should return all open and close times in CSV format
   
   "http://<host:port>/listOpenOnly/csv" should return open times only in CSV format
   
   "http://<host:port>/listCloseOnly/csv" should return close times only in CSV format

   "http://<host:port>/listAll/json" should return all open and close times in JSON format
   
   "http://<host:port>/listOpenOnly/json" should return open times only in JSON format
   
   "http://<host:port>/listCloseOnly/json" should return close times only in JSON format

* Also a query parameter to get top "k" open and close times. For examples, see below.

   "http://<host:port>/listOpenOnly/csv?top=3" should return top 3 open times only (in ascending order) in CSV format 
   
   "http://<host:port>/listOpenOnly/json?top=5" should return top 5 open times only (in ascending order) in JSON format

* A consumer program written in PHP


## Use

Clone the repo, cd to DockerRestAPI, and run `sudo docker-compose up`

The calculator is on port 5002, the api (api-service) is on port 5001, the consumer is on port 5000.

The "Submit" button sends the control data to the mongo database. The "Display" button displays all controls in the database.

requires: docker, docker-compose, python3 (and pip). Other requirements are installed into the container upon running.


## Changes from proj5

The calculator site functions the same. The API and comsumer are new.



### Author: Kyle Nielsen   Contact: kylen@uoregon.edu
