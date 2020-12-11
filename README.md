# LinkIt
URL Shortner Web Application using React.js for Frontend and Flask + MongoBD for Backend.

## Table of Content
- [General info](#general-info)
- [Technologies](#technologies)
- [Cloning Project](#clone-project)
- [Setup](#setup)
  + Server
  + Client


## General info
LinkIt will take your long URL and convert it into short link on a click. You can also create your own customize link and easily manage
your links at link-manager after you sign-up. Frontend of this app will be developed using React.js, CSS3 and Material-UI componenets. And, Backend 
is setup using Flask and MongoDB. To store your data in a secure fashion this app will be using Strong Parameters, Validators and Auth middlewares.


## Technologies
Project is created with:
* React version: ^16.13.1
* Redux version: ^4.0.5
* TypeScipt version: ^3.7.5
* Material-ui: ^4.11.2
* Axios: ^0.21.0
* Flask Version: ^1.1.2
* Pymongo Version: ^3.11.0
* Docker Version:  ^19.03.13
* Flask-Mail: ^0.9.1

## Clone Project
To clone this project click the green code button on the top right corner of this page. copy the HTTPs URL and open the local directory on command line / terminal for macOS. clone the project using follwing command on terminal:

- git clone < copied-link >

The project should be successfully cloned locally. Now you can follow setup to run the project locally.

# Setup
## Server
To run this project, Download or clone this repository locally and open the project using Visual Studio Code or PyCharm. First, you will need to download and install [Python](https://www.python.org/downloads/) latest version in your local machine, If you already have python installed you all set!. Run following commands in server directory to install all dependencies and run the server application successfully.

I strongly recommend to visit this [tutorial](https://www.nurmatova.com/dockerized-python-application.html) to Download and Install and get familiar with Docker before going further.

After Installation of docker in local machine open the project and type following commands. I would suggest to create new conda enviornment for this project.

- cd server
- conda create --name 'env-name'
![Creating New Enviorment](https://github.com/kmist1/URL_Shortener/blob/main/server/imgs/Screenshot%202020-11-26%20at%207.39.53%20PM.png)
- docker run -d -p 127.0.0.1:27018:27017 --name mongodb mongo
![After you run this command](https://github.com/kmist1/URL_Shortener/blob/main/server/imgs/Screenshot%202020-11-26%20at%207.42.17%20PM.png)
![downloading required files](https://github.com/kmist1/URL_Shortener/blob/main/server/imgs/Screenshot%202020-11-26%20at%207.41.42%20PM.png)
![You'll see this after successfully creating mongo container](https://github.com/kmist1/URL_Shortener/blob/main/server/imgs/Screenshot%202020-11-26%20at%207.49.09%20PM.png)

- pip install virtualenv  (Install virtual enviornment for Fask-Mail)
- pip install Flask-Mail (Install Flask Mail)

creating virtual enviornment using following commands:
- python3 -m venv env (macOS/Linux)
- py -m venv env (Windows)

activate the enviornment using following commands:
- .\env\Scripts\activate (Windows)
- source env/bin/activate (Linux/macOS)

To run the server on docker please use following commands:
- docker-compose build
- docker-compose up

![solve the error and run commands again](https://github.com/kmist1/URL_Shortener/blob/main/server/imgs/Screenshot%202020-11-26%20at%207.54.25%20PM.png)

Second command will create container under the name of mongodb (you can name it anything) and will also create mongo image and use that image for mongodb database.
here, mongodb running on port 27018 which we are mapping to 27017 which is out local machine mongodb (mongodb compass) to see the result.

Please use following commands if come accross Errors related to Address Already in use or MongoNetworkError:
- docker rm -f $(docker ps -aq) (will remove all of your containers)
- docker network rm $(docker network ls -q) (will remove all of your networks)

## Client
To run the client or frontend of the application please run the following commands in the client directory.

- First you'll need to download [Node](https://nodejs.org/en/download/).
- cd client
- npm install (To install all the dependancies from package.json)
- npm start

That's it!. Your app should be running on http://localhost:4000/






