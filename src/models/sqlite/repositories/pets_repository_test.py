from src.models.sqlite.entities.pets import PetsTable
from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from .pets_repository import PetsRepository


class MockConnection:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PetsTable)],
                    [
                        PetsTable(name='dog', type='dog'),
                        PetsTable(name='cat', type='cat'),
                    ]
                )
            ]
        )

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

    assert response[0].name == 'dog'
