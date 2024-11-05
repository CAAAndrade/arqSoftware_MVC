from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface


class PetCreatorController:
    def __init__(self, pets_repository: PetsRepositoryInterface) -> None:
        self.__pets_repository = pets_repository
