from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'Lord of the rings',
        'author': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'title': 'Harry Potter',
        'author': 'J.K Howling'
    }
]


@app.route('/books')
def listBooks():
    return jsonify(books)


@app.route('/books/<int:id>')
def getBook(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)


@app.route('/books/<int:id>', methods=['PUT'])
def editBook(id):
    changed_book = request.get_json()
    for index, book in enumerate(books):
        if book.get('id') == id:
            books[index].update(changed_book)
            return jsonify(books[index])


@app.route('/books/', methods=['POST'])
def createBook():
    book = request.get_json()
    books.append(book)
    return jsonify(books)


@app.route('/books/<int:id>', methods=['DELETE'])
def deleteBook(id):
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]
            return jsonify(books)


app.run(port=5000, host='localhost', debug=True)
