# graphql-python

This is a simple Flask application that provides a GraphQL API using SQLAlchemy and Graphene. It allows you to perform CRUD operations on a users table but dataset created manually.

## graphql
GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data. GraphQL provides a complete and understandable description of the data in your API, gives clients the power to ask for exactly what they need and nothing more, makes it easier to evolve APIs over time, and enables powerful developer tools.

### Schema
#### User
The User type represents a user in the users table.

### Fields
id: ID of the user.
name: Name of the user.
email: Email address of the user.

### Query
The Query type provides the following fields:
  * node: Fetches an object by its ID.
  * allUsers: Fetches a list of all users.

### Mutation
The Mutation type provides the following fields:

  * createUser: Creates a new user.

### Arguments
  * name (required): Name of the user.
  * email (required): Email address of the user.


#### Install enviroment as venv
```python3 -m venv venv```

#### Activate env
```source venv/bin/activate```

#### Install requirements
```pip install -r requirements.txt```

#### Run application
```python app.py```

