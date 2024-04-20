# basic_todo

## Project Overview
 This is a project for the Software Engineering course. The purpose of this project is to demonstrate the use of the Agile software development methodology.


## Features

- Create a task
- Delete a task
- Update a task
- Mark a task as complete
- View all tasks
- View a single task
- View completed tasks
- View incomplete tasks

## Database Schema

The database schema for the TODO List API is as follows:

|Field|Type|Description|
|-----|----|-----------|
|id|integer|The unique identifier for the task|
|task|text|The task description|
|description|text|The task description|
|completed|boolean|Whether the task is completed or not|
|created_at|datetime|The date and time the task was created|
|user_id| User id|

## API Endpoints

The API endpoints for the TODO List API are as follows:

|Method|Endpoint|Description|
|------|--------|-----------|
|GET|/api/tasks|Get all tasks|
|GET|/api/tasks/{id}|Get a single task|
|POST|/api/tasks|Create a new task|
|POST|/api/tasks/{id}|Update a task|
|POST|/api/tasks/{id}/complete|Mark a task as complete|
|POST|/api/tasks/{id}/delete|Delete a task|
|GET|/api/tasks/completed|Get all completed tasks|
|GET|/api/tasks/incomplete|Get all incomplete tasks|
