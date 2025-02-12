from fastapi import APIRouter
from api.routes import books

api_router = APIRouter()
api_router.include_router(books.router, prefix="/api/v1/books", tags=["books"])

#*from api.routes.books import router as books_router
#router.include_router(books_router, prefix="/api/v1")
