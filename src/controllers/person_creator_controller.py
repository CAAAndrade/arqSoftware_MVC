from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
import re


class PersonCreatorController:
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def create_person(self, person_info: dict) -> dict:
        first_name = person_info["first_name"]
        last_name = person_info["last_name"]
        age = person_info["age"]
        pet_id = person_info["pet_id"]

        self.__validate_first_and_last_name(first_name, last_name)

        self.__insert_person(first_name, last_name, age, pet_id)

        formatted_response = self.__format_response(person_info)
        return formatted_response

    def __validate_first_and_last_name(self, first_name: str, last_name: str) -> None:
        # Expressao Regular para caracteres que nao sao letras
        non_valid_characters = re.compile(r"[^a-zA-Z]")

        if non_valid_characters.search(first_name) or non_valid_characters.search(
            last_name
        ):
            raise Exception("Nome inválido")

    def __insert_person(
        self, first_name: str, last_name: str, age: int, pet_id: int
    ) -> None:
        self.__people_repository.insert_person(first_name, last_name, age, pet_id)

    def __format_response(self, person_info: dict) -> dict:
        return {"data": {"type": "person", "count": 1, "attributes": person_info}}