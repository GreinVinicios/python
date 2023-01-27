
# CommentApp
Python project containing an example an API which send comments.
The project is not connected to a DB, it's just an example.

  To run:
```python
python3 commentApp.py
```
The project will start listening on port 4040.

## Endpoints
| URL | Method | Description |
| - | - | - |
| localhost:4040/api/comment/list/;id/ | GET | Get the comment information |
| localhost:4040/api/comment/new/ | POST | Create one new coment |

> JSON example to be sent in POST
```json
{
"content_id": 1,
"email": "email@email.com",
"comment": "Test comment"
}
```

# Docker
Building and running the docker image
```bash
docker build . -t greinvinicios/commentapp:lts
docker run --network=host --name api --rm -d -p 4040:4040 greinvinicios/commentapp:lts
```