# LinkIt
URL Shortner Web Application using React.js for Frontend and Flask + MongoBD for Backend.

## Table of Content
* [General info](#general-info)
* [Technologies](#technologies)
* [Cloning Project](#clone-project)
* [Setup](#setup)

## General info
LinkIt will take your long URL and convert it into short link on a click. You can also create your own customize link and easily manage
your links at link-manager after you sign-up. Frontend of this app will be developed using React.js, CSS3 and Material-UI componenets. And, Backend 
is setup using Flask and MongoDB. To store your data in a secure fashion this app will be using Strong Parameters, Validators and Auth middlewares.


## Technologies
Project is created with:
* React version: ^16.13.1
* MondoDB version:  ^3.5.5
* Redux version: ^4.0.5
* TypeScipt version: ^3.7.5
* Flask Version: ^1.1.2

## Clone Project
To clone this project click the green code button on the top right corner of this page. copy the HTTPs URL and open the local directory on command line / terminal for macOS. clone the project using follwing command on terminal:

- git clone < copied-link >

The project should be successfully cloned locally. Now you can follow setup to run the project locally.

## Setup
To run this project, Download or clone this repository locally and open the project using Visual Studio Code or PyCharm. First, you will need to download and install [Python](https://www.python.org/downloads/) latest version in your local machine, If you already have python installed you all set!. Run following commands in server directory to install all dependencies and run the server application successfully.

- cd server
- pip install -e .
- python test.py

![To install dependencies](https://github.com/kmist1/URL_Shortener/blob/main/server/imgs/Screenshot%202020-11-11%20at%201.02.26%20AM.png)

I already have installed all dependency it is saying "Requirments already satisfied:...". In your case it would be different output than this. After installation test the app by running test.py file.

![To test code](https://github.com/kmist1/URL_Shortener/blob/main/server/imgs/Screenshot%202020-11-11%20at%201.24.00%20AM.png)


