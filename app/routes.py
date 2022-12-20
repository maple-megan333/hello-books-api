from flask import Blueprint, jsonify, abort, make_response, request
from .models.book import Book
from app import db

def validate_book(book_id):
    try: 
        book_id = int(book_id)
    except: 
        abort(make_response({"Message":f"book {book_id} is invalid"},400))
    
    book = Book.query.get(book_id)
    if not book:
        abort(make_response({"Message": f"book {book_id} not found"}, 400))
    return book
#helper functions 
def validate_book(book_id):
    try: 
        book_id = int(book_id)
    except: 
        abort(make_response({"Message":f"book {book_id} is invalid"},400))
    
    book = Book.query.get(book_id)
    if not book:
        abort(make_response({"Message": f"book {book_id} not found"}, 400))
    return book

#best_Books = [
#   Book(1, "A Great and Terrible Beauty", "Something wicked is lurking"),
#   Book(2, "Lightfall", "Get lost in a place"),
#   Book(3, "The Body Keeps the Score", "Rampant Abuse is a pandemic")
#]

books_bp = Blueprint("books", __name__, url_prefix="/books")
@books_bp.route("", methods=["POST"])
def handle_books():
    request_body = request.get_json()
    new_Book = Book(title=request_body["title"], 
    description=request_body["description"])
    db.session.add(new_Book)
    db.session.commit()
    return make_response(f"Book {new_Book.title} created", 201)

@books_bp.route("", methods=["GET"])
def read_all_books():
    books_response = []
    best_books=Book.query.all()
    for book in best_books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(books_response)

@books_bp.route("/<book_id", methods=["GET"])
def handle_book(book_id):
    book=validate_book(book_id)

    return {"id": book.id, 
    "title": book.title, 
    "description": book.description}


@books_bp.route("/<book_id>", methods=["PUT"])
def update_book(book_id):
    book=validate_book(book_id)
    request_body = request.get_json()
    book.title=request_body["title"]
    book.description = request_body["description"]

    db.session.commit()

    return make_response(f"Book # {book.id} sucessfully updated",  204)

@books_bp.route("/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    book=validate_book(book_id)

    db.session.delete(book)
    db.session.commit()

    return make_response(f"Book # {book.id} sucessfully deleted",  200)
