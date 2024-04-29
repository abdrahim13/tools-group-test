
# Decisions

## 1. I'm using Flask as the web framework
### Reasoning
I'm using Flask as the web framework because it is a lightweight and easy to use framework. It is also very flexible and has a lot of extensions available. I have experience with Flask and I think it is a good choice for this project.

## 2. SQLite with SQLAlchemy is used as the database
### Reasoning
I'm using SQLite with SQLAlchemy as the database because it is easy to set up and use. SQLite is a lightweight database that is perfect for small projects like this one.
SQLAlchemy is ORM that makes it easy to work with databases in Python.
SQLAlchemy is also compatible with other databases like MySQL, PostgreSQL, etc. so it is easy to switch to a different database if needed.


## 3.  Docker for containerization

### Reasoning
I'm using Docker for containerization that provides a consistent environment for development, testing, deployment package, run and deploy applications.


## 4.  UWSGI for serving the Flask app

### Reasoning
I'm using UWSGI for serving the Flask app because it is a fast and flexible application server with a lot of features for scaling and load balancing.
*Note: We could add also **nginx** for reverse proxy and load balancing.*


## 5.  Why API instead of GraphQL

### Reasoning
I'm using REST API instead of GraphQL because it is simpler and easier to work with for small projects like this one.
I would consider using GraphQL for larger projects where more complex queries and relations are needed.


