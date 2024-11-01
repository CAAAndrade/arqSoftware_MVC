import pytest
from src.models.sqlite.entities.pets import PetsTable
from unittest import mock
from sqlalchemy.orm.exc import NoResultFound
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from .pets_repository import PetsRepository


class MockConnection:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PetsTable)],
                    [
                        PetsTable(name="dog", type="dog"),
                        PetsTable(name="cat", type="cat"),
                    ],
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


# Mock para tratamento de erros, lancamos o erro que queremos testar
class MockConnectionNoResult:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise__no_result_found

    def __raise__no_result_found(self, *args, **kwargs):
        # *args e **kwargs sao os argumentos da funcao e irão receber todas as
        # propriedades enviadas para a funcao self.session.query.side_effect
        raise NoResultFound("No result found")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def test_list_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    response = repo.list_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)
    # acima verificasse se o mock_connection.session.query foi chamado uma vez para a classe PetsTable
    mock_connection.session.all.assert_called_once()
    # acima verificasse se o mock_connection.session.all foi chamado uma vez
    mock_connection.session.filter.assert_not_called()
    # acima verificasse se o mock_connection.session.filter não foi chamado

    assert response[0].name == "dog"


def test_delete_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    repo.delete_pets("petName")

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.filter.assert_called_once_with(PetsTable.name == "petName")
    mock_connection.session.delete.assert_called_once()


def test_list_pets_no_result():
    mock_connection = MockConnectionNoResult()
    repo = PetsRepository(mock_connection)
    response = repo.list_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()

    assert response == []


def test_delete_pet_error():
    mock_connection = MockConnectionNoResult()
    repo = PetsRepository(mock_connection)

    with pytest.raises(Exception):
        repo.delete_pets("petName")

    mock_connection.session.rollback.assert_called_once()
