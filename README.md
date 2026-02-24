# CMPSC431W-Web-Programming-Exercise

# Project Overview
A patient management web application built with Flask and SQLite. It allows users to add and delete patient records through HTML interfaces.

# Features
1. Add Patient - User can add patient to the database using {Firstname} {Lastname} format
2. Delete Patient - User can delete patient from the database using by specifying patient's {Firsrtname} {Lastname}

# Organization 
This code contains 3 html files that corresponds to 3 web pages and a python file for Flask. 
1. index.html - this file contains the code for the landing page
2. addPatient.html - this file contains the code for the add patient page
3. deletePatient.html - this file contains the code for the delete patient page
4. app.py - this file contains the Flask code that connect the html pages and routing necessary for the web app and handle the database

# Requirement
1. Python 3.11.9
2. Flask
3. Pycharm

# How to run the web app
1. Open PyCharm and navigate to the project folder.
2. To run this project, user need to have Flask install inside the IDE. To install flask, user can run ``pip install Flask`` inside the terminal
3. Once the packet is installed, user can run the web app by running ``python app.py``.
4. The terminal will specify where the program is running, for example ``Running on http://127.0.0.1:5000``. Click this link to open the web app.

# Reference and Source
This project is implemented using the element and component from Bootstrap documentation pages and W3School
[https://getbootstrap.com/docs/5.3/getting-started/introduction/](url)
[https://www.w3schools.com/html/](url)
