from tests import client


def setup_test_book():
    """Ensure a book with id=1 is created before running other tests."""
    book_payload = {
        "id": 1,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "publication_year": 1937,
        "genre": "Fantasy",
    }
    client.post("/books/", json=book_payload)


def test_get_all_books():
    setup_test_book()
    response = client.get("/books/")
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_get_single_book():
    setup_test_book()
    response = client.get("/books/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "The Hobbit"
    assert data["author"] == "J.R.R. Tolkien"


def test_create_book():
    new_book = {
        "id": 2,
        "title": "Harry Potter",
        "author": "J.K. Rowling",
        "publication_year": 1997,
        "genre": "Fantasy",
    }
    response = client.post("/books/", json=new_book)
    assert response.status_code == 201
    assert response.json()["id"] == 2


def test_update_book():
    setup_test_book()
    updated_book = {
        "id": 1,
        "title": "The Hobbit: An Unexpected Journey",
        "author": "J.R.R. Tolkien",
        "publication_year": 1937,
        "genre": "Fantasy",
    }
    response = client.put("/books/1", json=updated_book)
    assert response.status_code == 200
    assert response.json()["title"] == "The Hobbit: An Unexpected Journey"


def test_delete_book():
    setup_test_book()
    response = client.delete("/books/1")
    assert response.status_code == 204

    response = client.get("/books/1")
    assert response.status_code == 404

# Testing CI Pipeline Trigger
