from flask import Blueprint, jsonify, abort, make_response
from .book import Book


best_Books = [
    Book(1, "A Great and Terrible Beauty", "Something wicked is lurking"),
    Book(2, "Lightfall", "Get lost in a place"),
    Book(3, "The Body Keeps the Score", "Rampant Abuse is a pandemic")
]

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET"])
def handle_books():
    books_response = []
    for book in best_Books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(books_response)

def validate_book(book_id):
    try: 
        book_id = int(book_id)
    except: 
        abort(make_response({"Message":f"book {book_id} is invalid"},400))
    
    for book in best_Books:
        if book.id==book_id:
            return book
    abort(make_response({"Message": f"book {book_id} not found"}, 400))


@books_bp.route("/<book_id", methods=["GET"])
def handle_book(book_id):
    book=validate_book(book_id)

    return {"id": book.id, 
    "title": book.title, 
    "description": book.description}
