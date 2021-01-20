# rest-todo

## Table of content
 - [installation](#installation)
 - [deploy using docker-compose](#deploy-using-docker-compose)
 - [API](#api)


## installation
1. Clone the repo
    ```shell script
    git clone https://github.com/nabakirov/rest-todo.git
    ```
2. Step into repo dir
    ```shell script
    cd rest-todo
    ```
3. Install dependencies   
    using [pipenv](https://github.com/pypa/pipenv)
    ```shell script
    pipenv install && pipenv shell
    ```
    or using virtualenv
    ```shell script
    python3 -m virtualenv venv && source venv/bin/activate && pip install -r requirements.txt
    ```
4. Set environment variables   
    - SECRET_KEY=secret   
    - RESOURCES_DIR=/path/to/dir/  
    - DEBUG=True/False  
    - DATABASE_URL=sqlite:///secret/db.sqlite3  

5. Apply migrations
    ```shell script
    python manage.py migrate
    ```
5. Run   
    using gunicorn
    ```shell script
    gunicorn -w 1 -b 0.0.0.0:8000 rest_todo.wsgi
    ```
   or start development server
   ```shell script
    python manage.py runserver
    ```
   

## deploy using docker-compose
1. Clone the repo
    ```shell script
    git clone https://github.com/nabakirov/rest-todo.git
    ```
2. Set environment variables   
    - SECRET_KEY=secret   
    - DEBUG=True/False  
    - POSTGRES_PASSWORD=password (postgres user password)
    - DATABASE_USER=some_user
    - DATABASE_PASSWORD=password (user's database password)
    - PORT=8000
3. Install and run
    ```shell script
    cd compose && docker-compose up -d
    ```

## API
- [Authorization](#authorization)
- [Pagination](#pagination)
- [Registration](#registration)
- [Login](#login)
- [Refresh token](#refresh-token)
- [Profile](#profile)
- [List categories](#list-categories)
- [Tree categories](#tree-categories)
- [Retrieve category](#retrieve-category)
- [Create category](#create-category)
- [Update category](#update-category)
- [Delete category](#delete-category)
- [List todo's](#list-todos)
- [Retrieve todo](#retrieve-todo)
- [Create todo](#create-todo)
- [Update todo](#update-todo)
- [Delete todo](#delete-todo)

## Authorization
You will be given access and refresh tokens  
You have to submit access token from login or registration in headers of request   
```Authorization: Bearer <access token>```   
access token lives short time, but can be refreshed by refresh token   

## Pagination
to control pagination use query params
```
?limit=100&offset=400
```
paginated response will look like
```json5
{
  "count": "int",            // count of all elements
  "next": "str or null",     // url for next "page"   
  "previous": "str or null", // url for previous "page"   
  "results":[]               // data
}
```
### registration
#### POST */v1/registration/*
##### access - *public*
request body   
```json5
{
	"username": "str",  // required
	"password": "str",  // required
	"name": "str"       // nullable
}
```
response
```json5
{
  "user": {
    "id": "int",
    "username": "str",
    "name": "str",  // nullable
    "creation_date": "str", // timestamp
    "last_login": "str" // timestamp
  },
  "refresh": "str", // jwt refresh token
  "access": "str"   // jwt access token
}
```
### login
#### POST */v1/login/*
##### access - *public*
request body   
```json5
{
	"username": "str",  // required
	"password": "str",  // required
}
```
response
```json5
{
  "user": {
    "id": "int",
    "username": "str",
    "name": "str",  // nullable
    "creation_date": "str", // timestamp
    "last_login": "str" // timestamp
  },
  "refresh": "str", // jwt refresh token
  "access": "str"   // jwt access token
}
```
### refresh token
#### POST */v1/refresh_token/*
##### access - *public*
request body   
```json5
{
	"refresh": "str",  // required
}
```
response
```json5
{
  "access": "str"   // jwt access token
}
```

### profile
#### GET */v1/profile/*
##### access - *authorized*
response
```json5
{
    "id": "int",
    "username": "str",
    "name": "str",  // nullable
    "creation_date": "str", // timestamp
    "last_login": "str" // timestamp
}
```

### list categories
#### GET */v1/categories/*
##### access - *authorized*
request query parameters:
- parent_id=int or null // filter categories by parent_id   
- search=str   
paginated response
```json5
{
    "id": "int",
    "title": "str",
    "creation_date": "str", // timestamp
    "parent": "int" // nullable, foreign key
}
```
### tree categories 
#### GET */v1/categories/tree/*
##### access - *authorized*
response
```json5
{
    "id": "int",
    "title": "str",
    "creation_date": "str", // timestamp
    "parent": "int", // nullable, foreign key
    "children": [
      {
        ...,
        "children": []
      }   
    ]   
}
```

### retrieve category
#### GET */v1/categories/{id}/*
##### access - *authorized*
response
```json5
{
    "id": "int",
    "title": "str",
    "creation_date": "str", // timestamp
    "parent": "int" // nullable, foreign key
}
```

### create category
#### POST */v1/categories/*
##### access - *authorized*
request
```json5
{
	"title": "str", // required
	"parent": "int" // nullable
}
```
response
```json5
{
    "id": "int",
    "title": "str",
    "creation_date": "str", // timestamp
    "parent": "int" // nullable, foreign key
}
```

### update category
#### PATCH/PUT */v1/categories/{id}/*
##### access - *authorized*
request
```json5
{
	"title": "str",
	"parent": "int" // nullable
}
```
response
```json5
{
    "id": "int",
    "title": "str",
    "creation_date": "str", // timestamp
    "parent": "int" // nullable, foreign key
}
```

### delete category
#### DELETE */v1/categories/{id}/*
##### access - *authorized*
response status code 204

### list todo's
#### GET */v1/todo/*
##### access - *authorized*
request query parameters:
- category_id=int or null // filter todo's by category_id   
- schedule=str // YYYY-MM-DD
- is_done=True/False
- search=str   
paginated response
```json5
{
  "id": "int",
  "title": "str",
  "category": "int", // nullable
  "creation_date": "str", // timestamp
  "schedule": "str", // nullable, "YYYY-MM-DD"
  "is_done": "bool"
}
```

### retrieve todo
#### GET */v1/todo/{id}/*
##### access - *authorized*
response
```json5
{
  "id": "int",
  "title": "str",
  "category": {
    "id": "int",
    "title": "str",
    "creation_date": "str", // timestamp
    "parent": "int" // nullable
  },
  "description": "str", // nullable
  "creation_date": "str", // timestamp
  "schedule": "str", // nullable, "YYYY-MM-DD"
  "is_done": "bool"
}
```

### create todo
#### POST */v1/todo/*
##### access - *authorized*
request
```json5
{
    "title": "str", // required
    "category": "int", // nullable
    "description": "str", // nullable
    "schedule": "str" // nullable, "YYYY-MM-DD"
}
```
response
```json5
{
  "id": "int",
  "title": "str",
  "category": "int", // nullable
  "description": "str", // nullable
  "creation_date": "str", // timestamp
  "schedule": "str", // nullable, "YYYY-MM-DD"
  "is_done": "bool"
}
```
### update todo
#### PATCH/PUT */v1/todo/{id}/*
##### access - *authorized*
request
```json5
{
    "title": "str",
    "category": "int", // nullable
    "description": "str", // nullable
    "schedule": "str" // nullable, "YYYY-MM-DD"
}
```
response
```json5
{
  "id": "int",
  "title": "str",
  "category": "int", // nullable
  "description": "str", // nullable
  "creation_date": "str", // timestamp
  "schedule": "str", // nullable, "YYYY-MM-DD"
  "is_done": "bool"
}
```
### delete todo
#### DELETE */v1/todo/{id}/*
##### access - *authorized*
response status code 204
