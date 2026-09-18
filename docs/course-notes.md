# Web and APIs — Course Notes

## 1. HTTP

HTTP (Hypertext Transfer Protocol) is a protocol used for communication between a client and a server.

A client sends an HTTP request to a server, and the server sends an HTTP response back.

Example:

Client → HTTP Request → Server  
Client ← HTTP Response ← Server

---

## 2. HTTP Methods

HTTP methods describe the action that the client wants to perform.

### GET

GET is used to retrieve or read data from the server.

Example:

GET /tasks

### POST

POST is used to create new data on the server.

Example:

POST /tasks

### PATCH

PATCH is used to partially update existing data.

Example:

PATCH /tasks/1

### DELETE

DELETE is used to remove existing data.

Example:

DELETE /tasks/1

### Summary

| Method | Purpose |
|---|---|
| GET | Read data |
| POST | Create data |
| PATCH | Update data |
| DELETE | Delete data |

---

## 3. API

API (Application Programming Interface) allows different software systems to communicate with each other.

A web API allows a client application to send requests to a server and receive data or results.

Example:

GET /tasks

The client requests the list of tasks, and the server returns the requested data.

---

## 4. Endpoint

An endpoint is a specific URL through which an API provides a particular operation or resource.

Examples:

GET /tasks  
POST /tasks  
PATCH /tasks/1  
DELETE /tasks/1

Each endpoint represents a specific operation.

---

## 5. URL

A URL (Uniform Resource Locator) identifies the location of a resource on the web.

Example:

https://example.com/tasks

An API URL can contain a resource and sometimes an identifier.

Example:

/tasks/5

Here, 5 can identify a specific task.

---

## 6. JSON

JSON (JavaScript Object Notation) is a common format used to exchange structured data between a client and a server.

Example:

{
  "id": 1,
  "title": "Complete assignment",
  "status": "todo"
}

JSON stores information using key-value pairs.

---

## 7. HTTP Request

An HTTP request is sent by the client to the server.

A request can contain:

- HTTP method
- URL
- Headers
- Request body

Example:

POST /tasks

Content-Type: application/json

Request body:

{
  "title": "Complete assignment"
}

---

## 8. HTTP Response

An HTTP response is returned by the server after processing a request.

A response can contain:

- Status code
- Headers
- Response body

Example:

HTTP/1.1 200 OK

Response body:

{
  "id": 1,
  "title": "Complete assignment",
  "status": "todo"
}

---

## 9. HTTP Status Codes

HTTP status codes indicate the result of an HTTP request.

### 2xx — Successful Requests

#### 200 OK

The request was successfully processed.

#### 201 Created

A new resource was successfully created.

Example:

POST /tasks → 201 Created

---

### 4xx — Client Errors

#### 400 Bad Request

The request contains invalid or incorrect data.

#### 401 Unauthorized

Authentication is required or the user has not been properly authenticated.

#### 403 Forbidden

The user is authenticated but does not have permission to perform the requested action.

#### 404 Not Found

The requested resource could not be found.

---

### 5xx — Server Errors

#### 500 Internal Server Error

The server encountered an unexpected problem while processing the request.

---

## 10. 401 vs 403

These status codes are important for authentication and authorization.

### 401 Unauthorized

The client has not provided valid authentication credentials.

Example:

User tries to access /tasks without logging in.

### 403 Forbidden

The user is authenticated but does not have permission to perform the requested action.

Example:

A user tries to modify another user's task.

### Simple Difference

401 → Authentication problem  
403 → Permission problem

---

## 11. Authentication

Authentication is the process of verifying the identity of a user.

Example:

Email + Password  
↓  
Authentication  
↓  
User is logged in

A common authentication flow is:

1. User registers an account.
2. User provides login credentials.
3. Server verifies the credentials.
4. Server authenticates the user.
5. User can access protected resources.

---

## 12. Authorization

Authorization determines what an authenticated user is allowed to do.

Example:

User A → Can modify User A's task  
User A → Cannot modify User B's task

Authentication answers:

Who are you?

Authorization answers:

What are you allowed to do?

---

## 13. Database-Backed Application

A database-backed application stores application data in a database.

For a task management API, the database can store:

- Users
- Tasks
- Task status
- Task ownership

Example:

Client  
↓  
API  
↓  
Business Logic  
↓  
Database

---

## 14. Validation

Validation checks whether the input provided by a user is valid before processing it.

Examples of validation:

- Required fields must not be empty.
- Email must have a valid format.
- Password must meet required rules.
- Task title must not exceed the allowed length.
- Task status must be one of the allowed values.

Validation helps prevent invalid data from entering the application.

---

## 15. Structured JSON Errors

APIs should return errors in a consistent and structured format.

Example:

{
  "error": "ValidationError",
  "message": "Task title is required"
}

A structured error response makes it easier for clients to understand and handle errors.

---

## 16. REST-Style API

A REST-style API uses HTTP methods and resources to perform operations.

Example:

GET /tasks  
POST /tasks  
PATCH /tasks/1  
DELETE /tasks/1

The resource in these examples is a task.

---

## 17. Environment Variables

Environment variables are used to store configuration values outside the source code.

Examples:

DATABASE_URL  
SECRET_KEY  
API_KEY

Sensitive values such as passwords, secret keys and API credentials should not be committed directly to GitHub.

A .env.example file can show which variables are required without containing real secret values.

Example:

DATABASE_URL=  
SECRET_KEY=

---

## 18. API Testing

API testing verifies that API endpoints work correctly.

API testing can check:

- Request method
- URL
- Request body
- Status code
- Response body
- Authentication
- Authorization
- Validation
- Error handling

Tools such as Postman can be used to send API requests and inspect responses.

---

## 19. API Integration Testing

Integration tests verify that different parts of an application work together.

For example:

API  
↓  
Authentication  
↓  
Business Logic  
↓  
Database

An integration test can verify that creating a task through the API correctly stores the task in the database and returns the expected response.

---

## Key Points

- HTTP allows clients and servers to communicate.
- GET reads data.
- POST creates data.
- PATCH updates data.
- DELETE removes data.
- APIs provide a way for software systems to communicate.
- JSON is commonly used for structured API data.
- 2xx status codes indicate successful requests.
- 4xx status codes indicate client-side or request errors.
- 5xx status codes indicate server-side errors.
- Authentication verifies user identity.
- Authorization controls user permissions.
- Validation prevents invalid input.
- Environment variables keep configuration and secrets outside source code.
- API testing checks whether endpoints behave as expected.se.



