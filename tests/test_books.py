from tests import client


def test_create_book():
    new_book = {
        "id": 1,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "publication_year": 1937,
        "genre": "Fantasy",
    }
    response = client.post("/books/", json=new_book)
    assert response.status_code == 201


def test_get_all_books():
    test_create_book()  # Ensure data exists before testing
    response = client.get("/books/")
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_get_single_book():
    test_create_book()  # Ensure book exists before testing
    response = client.get("/books/1")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "The Hobbit"
    assert data["author"] == "J.R.R. Tolkien"


def test_update_book():
    test_create_book()  # Ensure book exists before testing
    updated_book = {
        "id": 1,
        "title": "The Hobbit: An Unexpected Journey",
        "author": "J.R.R. Tolkien",
        "publication_year": 1937,
        "genre": "Fantasy",
    }
    response = client.put("/books/1", json=updated_book)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "The Hobbit: An Unexpected Journey"


def test_delete_book():
    test_create_book()  # Ensure book exists before testing
    response = client.delete("/books/1")
    assert response.status_code == 204

    response = client.get("/books/1")
    assert response.status_code == 404
