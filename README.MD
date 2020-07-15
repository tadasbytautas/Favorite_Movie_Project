# The Favorite Movie Project
## Recources
###### GIT: https://github.com/tadasbytautas/Favorite_Movie_Project
###### TRELLO: https://trello.com/b/q5yqVhCr/favorite-movie-project

## Content
* Project Description
* Functionality
* Entity Relationship Diagram (ERD)
* Tech Stack
* Front-End Design
* Risk Assessment
* Difficulties
* Ongoing Issues
* Future Improvements
* Authors

## Project Description

This is a small CRUD application built with Python Flask. As a user you are able to **Create**, **Read**, **Update** and **Delete** information on it. Project was designed in the way that different users would able register and add their favorite movies on the main board for everyone to see.

##### _**Minimum requirements**_
* A Trello board (or equivalent Kanban board tech) with full expansion
on user stories, use cases and tasks needed to complete the project.
It could also provide a record of any issues or risks that you faced
creating your project.
* A relational database used to store data persistently for the
project, this database needs to have at least 2 tables in it, to
demonstrate your understanding, you are also required to model a
relationship.
* Clear Documentation from a design phase describing the architecture
you will use for you project as well as a detailed Risk Assessment.
A functional CRUD application created in Python, following best
practices and design principles, that meets the requirements set on
your Kanban Board
* Fully designed test suites for the application you are creating, as
well as automated tests for validation of the application. You must
provide high test coverage in your backend and provide consistent
reports and evidence to support a TDD approach.
* A functioning front-end website and integrated API's, using Flask.
Code fully integrated into a Version Control System using the
Feature-Branch model which will subsequently be built through a CI
server and deployed to a cloud-based virtual machine.

## Functionality

Project based on CRUD, below are some user stories to support that functionality.

- As a user I must to be able to see all the post made on the main board.
- As a user I must to be able to add new movies to the main board.
- As a user I must to be able edit my post that were made previously.
- As a user I must to be able to delete movie from the main board.

##### Additional functionality (_not required by task but nice to have_)

- As a user I should be able to register new account.
- As a user I should be able to login to newly registered account.
- As a user I should be able to delete my OWN posts only. (posts made by other account should not be accessible for deletion or edits).

## Entity Relationship Diagram (ERD)

This is simple ERD diagram to show one to many relationship between two data tables, Users and Posts made by registered accounts.

![ERD](/images/ERD.jpg)  

## Tech Stack

Technologies used to get Favorite Movie Project to where is it right now.

- Trello - Project Management
- Git / GitHub - Version Control System
- Google Cloud MySQL - Hosting Database
- Google Cloud WM - Hosting Linux Ubuntu Instance
- Nginx - Web Server 
- Jenkins - CI functionality
- Python 3 - Backend Functionality
- List of Modules:
    * Flask
    * Jinja2
    * Flask-SQLAlchemy
    * SQLAlchemy
    * pymysql
    * WTForms
    * Flask-WTF
    * Flask-Bcrypt
    * email_validator
    * flask-login
- Bootstrap 4 - Minimal Frontend Styling

## Front-End Design

Bootstrap 4 was used to build most of the styling. See below for screenshots of each individual page.
