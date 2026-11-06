# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API in Python using FastAPI by creating routes, handling JSON data, and validating user input.

## 📝 Tasks

### 🛠️ Set Up the API Application

#### Description
Create a FastAPI application and define a basic item resource that can be accessed through HTTP endpoints.

#### Requirements
Completed program should:

- Import `FastAPI` and create an app instance.
- Define a root route that returns a welcome message.
- Create a small in-memory list of items to represent stored data.
- Run the app with Uvicorn using `uvicorn app:app --reload`.
- Example response:
  ```json
  {
    "message": "Welcome to the Item API"
  }
  ```

### 🛠️ Build CRUD Endpoints

#### Description
Implement the basic create, read, update, and delete operations for an item resource.

#### Requirements
Completed program should:

- Add a `GET /items` route that returns all items.
- Add a `GET /items/{item_id}` route that returns a single item.
- Add a `POST /items` route that accepts JSON data and creates a new item.
- Add a `PUT /items/{item_id}` route that updates an existing item.
- Add a `DELETE /items/{item_id}` route that removes an item.
- Return JSON data in a clean, readable format.

### 🛠️ Add Validation and Error Handling

#### Description
Improve the API so it validates incoming data and handles missing items gracefully.

#### Requirements
Completed program should:

- Use a Pydantic model for item data validation.
- Require fields such as `name`, `price`, and `in_stock`.
- Return a `404` error when an item does not exist.
- Return a `201` status code when a new item is created.
- Example request:
  ```json
  {
    "name": "Keyboard",
    "price": 49.99,
    "in_stock": true
  }
  ```
