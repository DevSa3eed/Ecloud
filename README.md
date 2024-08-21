# Flask CRUD Service

This is a simple CRUD (Create, Read, Update, Delete) service built using Python and Flask. The service manages `User` objects with `username`, `password`, and `active` fields. This project serves as an example of implementing basic CRUD operations in a RESTful API.

## Features

- **Create**: Add new users to the system.
- **Read**: Retrieve details of existing users.
- **Update**: Modify user details.
- **Delete**: Remove users from the system.

## Requirements

- Python 3.x
- Flask

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <your_repository_url>
   cd flask_crud_service
   ```

2. **Create a Virtual Environment (Optional but Recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Service

1. **Start the Flask Server**:
   ```bash
   python app.py
   ```

2. **Access the Service**:
   The service will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### 1. Create a User
   - **Endpoint**: `/users`
   - **Method**: `POST`
   - **Description**: Adds a new user.
   - **Request Body**:
     ```json
     {
       "username": "john_doe",
       "password": "12345",
       "active": true
     }
     ```
   - **Response**: Returns the created user object with a generated user ID.

### 2. Get a User
   - **Endpoint**: `/users/<user_id>`
   - **Method**: `GET`
   - **Description**: Retrieves details of a user by ID.
   - **Response**: Returns the user object.

### 3. Update a User
   - **Endpoint**: `/users/<user_id>`
   - **Method**: `PUT`
   - **Description**: Updates the details of a user.
   - **Request Body**: Similar to the `POST` request.
   - **Response**: Returns the updated user object.

### 4. Delete a User
   - **Endpoint**: `/users/<user_id>`
   - **Method**: `DELETE`
   - **Description**: Deletes a user by ID.
   - **Response**: Returns a success message.

## Testing the API

You can test the API using tools like [Postman](https://www.postman.com/) or `curl` commands as shown in the example below:

- **Create a User**:
  ```bash
  curl -X POST http://127.0.0.1:5000/users -H "Content-Type: application/json" -d '{"username": "john_doe", "password": "12345", "active": true}'
  ```

- **Get a User**:
  ```bash
  curl -X GET http://127.0.0.1:5000/users/1
  ```

- **Update a User**:
  ```bash
  curl -X PUT http://127.0.0.1:5000/users/1 -H "Content-Type: application/json" -d '{"username": "john_doe", "password": "54321", "active": false}'
  ```

- **Delete a User**:
  ```bash
  curl -X DELETE http://127.0.0.1:5000/users/1
  ```

## License

This project is licensed under the MIT License.

---

Feel free to adjust the content based on your preferences and any additional details you want to include.
