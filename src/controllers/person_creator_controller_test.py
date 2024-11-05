from .person_creator_controller import PersonCreatorController
import pytest


class MockPeopleRepository:
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int):
        pass


def test_create_person():
    person_creator_controller = PersonCreatorController(MockPeopleRepository())
    person_info = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 30,
        "pet_id": 1,
    }
    person = person_creator_controller.create_person(person_info)
    assert person == {"data": {"type": "person", "count": 1, "attributes": person_info}}

def test_create_error():
    person_info = {
            "first_name": "John123",
            "last_name": "Doe",
            "age": 30,
            "pet_id": 1,
        }

    person_creator_controller = PersonCreatorController(MockPeopleRepository()) 

    with pytest.raises(Exception):
        person_creator_controller.create_person(person_info)

    # se o teste passar é porque a logica do teste do erro está correta

