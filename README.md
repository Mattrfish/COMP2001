This repository contains the source code for the Trail Microservice for COMP2001-CW2.

This is a brief of what you will find in the Report:

Introduction:
The microservice allows users to explore various trails, 
manage trail details, and track its features. It uses a RESTful API for CRUD operations, user authentication,
and database interaction. 

The service is deployed using Docker.
Github: CW2/comp2001_flask
Docker Image: mattrfish/2001_flask

Features: CRUD Operations, User Authentication, Trail Management, and RESTful Design.

Architecture Overview: Database to store and manage trail data, token based authentication for secure access.
EndPoints - /trails , /trails/{TrailId} , /features , /features/{FeatureId} , 
/trails/{TrailId}/features , /trails/{TrailId}/features/{FeatureId} .

Key Components: Trails - Details such as difficulty, location, length and elevation gain.
Features - Specific attributes like dog-friednly, bike trail, ponds, dirt paths etc.
Users - Roles include Users (Read-only) and Admins (Full CRUD access)

LSEP: Legal - Complicance with GDPR, secure storage and handling of user credentials.
Social and Ethical - Access control ensures proper role based permissions.
Professional - Code quality adheres to industry standards, and version controlled is maintained. 

Testing: Authentication, RBAC for CRUD, error handling
Areas for improvement: Enhanced security Measures, Automatic assignment of owner IDs for trail creation,
tracking between location points. 

Conclusion: The Trail microservice successfully achieves its goals of secure and efficient trail management. While future
improvements are possible, the current implementation adheres to the core functions, RESTful principles and professional standards.

