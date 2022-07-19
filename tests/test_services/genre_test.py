from unittest.mock import MagicMock

import pytest

from DAO.genre import GenreDAO
from DAO.models.genre import Genre
from services.genre_service import GenreService


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    g1 = Genre(id=1, name='Романтика')
    g2 = Genre(id=2, name='Научные фильмы')
    g3 = Genre(id=3, name='История')

    genres = {1: g1, 2: g2, 3: g3}

    genre_dao.get_one = MagicMock(side_effect=genres.get)
    genre_dao.get_all = MagicMock(return_value=genres.values())
    genre_dao.create = MagicMock(return_value=Genre(id=1, name='Романтика'))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert genres is not None
        assert len(genres) > 0

    def test_create(self):
        g1 = {'name': 'Романтика'}
        genre = self.genre_service.create(g1)
        assert genre is not None
        assert genre.id is not None

    def test_update(self):
        g1 = {'id': 1, 'name': 'Новое имя'}
        self.genre_service.update(g1)

    def test_part_update(self):
        g1 = {'id': 1, 'name': 'New Name'}
        self.genre_service.update(g1)

    def test_delete(self):
        self.genre_service.delete(1)
