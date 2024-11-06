from src.models.sqlite.repositories.pets_repository import PetsRepositoryInterface

class PetDeleterController:
    def __init__(self, pets_repository: PetsRepositoryInterface) -> None:
        self.__pets_repository = pets_repository

    def delete_pet(self, name: str) -> None:
        self.__pets_repository.delete_pets(name)


# nos protocolos de htttp metodos de delete não trazem nenhum return