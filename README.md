[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=22988088)
# CSSE6400 Week 1 Practical

Construction of a simple HTTP server in Python.

Please see the [instructions](https://csse6400.uqcloud.net/practicals/week01.pdf) for more details.

Update this README file with appropriate information about your project,
including how to run it.

There are [resources](https://www.makeareadme.com) available to help you write a good README file.


API Endpoints

This project implements the following RESTful endpoints:

Method	Path	Description
GET	/api/v1/health	Check service status, returns {"status": "ok"}
GET	/api/v1/todos	Retrieve a list of all todo items
GET	/api/v1/todos/{id}	Retrieve details of a specific todo item by ID
POST	/api/v1/todos	Create a new todo item (requires title in the request body)
PUT	/api/v1/todos/{id}	Update an existing todo item
DELETE	/api/v1/todos/{id}	Delete a specified todo item
Testing Guide

You can test the API using the endpoints.http file (with the VS Code REST Client extension) or curl commands:

curl -X GET http://localhost:6400/api/v1/health

AI Statement

I hereby declare that AI tools were used to assist in the development of this project.

Tools Used: ChatGPT / Claude / Google AI
Purpose of Use: AI was primarily used to assist in understanding the routing logic of Flask Blueprints, guide Poetry environment configuration, and troubleshoot syntax errors during debugging.
Academic Integrity Declaration

Assistance, Not Ghostwriting: AI served only as a technical advisor, used to explain complex architectural concepts (such as the relationship between the OSI model and the HTTP protocol) and to assist in debugging. All routing logic, code structure design, and business logic implementation were independently completed by me based on a full understanding of the material.
Independent Work: I did not use AI to generate entire segments of business logic code for direct submission. All deliverables of this project reflect my mastery of the Week 01 course content.
Compliance: This statement is intended to ensure transparency in the use of technology and fully complies with UQ’s policies on the responsible use of generative AI.