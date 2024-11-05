from src.models.sqlite.repositories.people_repository import PeopleRepositoryInterface
from src.models.sqlite.entities.people import PeopleTable


class PersonFinderController:
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def find_person(self, person_id: int) -> dict:
        person = self.__find_person_in_db(person_id)
        return self.__format_response(person)

    def __find_person_in_db(self, person_id: int) -> PeopleTable:
        person = self.__people_repository.get_person(person_id)
        if not person:
            raise Exception("Person not found")
        return person

    def __format_response(self, person: PeopleTable) -> dict:
        return {
            "data": {
                "type": "person",
                "count": 1,
                "attributes": {
                    "first_name": person.first_name,
                    "last_name": person.last_name,
                    "pet_name": person.pet_name,
                    "pet_type": person.pet_type,
                },
            }
        }
