from flask import Blueprint, jsonify
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