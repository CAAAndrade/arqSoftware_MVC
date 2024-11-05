from src.controllers.pet_lister_controller import PetListerController
from src.models.sqlite.entities.pets import PetsTable


class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="max", type="dog", id=1),
            PetsTable(name="miau", type="cat", id=2),
        ]
    
def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list_pets()

    expected_response = {
        "data": {
            "type": "pets",
            "count": 2,
            "attributes": [
                {"name": "max", "type": "dog", "pet_id": 1},
                {"name": "miau", "type": "cat", "pet_id": 2},
            ],
        }
    }

    assert response == expected_response
