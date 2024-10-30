from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pets_repository import PetsRepository


db_connection_handler.connect_to_db()


def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print()
    print(response)