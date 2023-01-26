# API

Python project containing an example of an API.
The project is not connected to a DB, it's just an example using a default JSON object.

To run:
```python
python3 main.py
```

The project will start listening on port 5000.

## Endpoints
| URL | Method | Description |
| - | - | - |
| localhost:5000/books/ | GET | Get the list of books |
| localhost:5000/books/:id | GET | Get information of disired book |
| localhost:5000/books/:id | PUT | Update one book |
| localhost:5000/books/ | POST | Create a new book |
| localhost:5000/books/:id | DELETE | Delete one book | 

> JSON example to be sent in PUT/POST
```json
{
  "id": 2,
  "title": "Harry Potter",
  "author": "J.K. Howling"
}
```