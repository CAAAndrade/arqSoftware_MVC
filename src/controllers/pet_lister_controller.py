from src.models.sqlite.repositories.pets_repository import PetsRepositoryInterface
from src.models.sqlite.entities.pets import PetsTable


class PetListerController:
    def __init__(self, pets_repository: PetsRepositoryInterface) -> None:
        self.__pets_repository = pets_repository

    def list_pets(self):
        pets = self.__get_pets_in_db()
        response = self.__format_response(pets)
        return response

    def __get_pets_in_db(self) -> list[PetsTable]:
        pets = self.__pets_repository.list_pets()
        return pets

    def __format_response(self, pets: list[PetsTable]) -> dict:
        formatted_pets = []

        for pet in pets:
            formatted_pets.append(
                {"name": pet.name, "type": pet.type, "pet_id": pet.id}
            )

        return {
            "data": {
                "type": "pets",
                "count": len(formatted_pets),
                "attributes": formatted_pets,
            }
        }
