from unittest.mock import MagicMock

import pytest

from DAO.movie import MovieDAO
from DAO.models.movie import Movie
from services.movie_service import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    m1 = Movie(id=1, title='Первый фильм', description='Description',
               trailer='link', year=2010, rating=8.8, genre_id=1, diretor_id=1)
    m2 = Movie(id=2, title='Второй фильм', description='Description',
               trailer='link', year=2010, rating=8.8, genre_id=1, director_id=1)
    m3 = Movie(id=3, title='Третий фильм', description='Description',
               trailer='link', year=2010, rating=8.8, genre_id=1, diretor_id=1)

    movies = {1: m1, 2: m2, 3: m3}

    movie_dao.get_one = MagicMock(side_effect=movies.get)
    movie_dao.get_all = MagicMock(return_value=movies.values())
    movie_dao.create = MagicMock(return_value=Movie(id=1, title='Первый фильм'))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert movies is not None
        assert len(movies) > 0

    def test_create(self):
        m1 = {
            'title': 'Первый фильм',
            'description': 'Description',
            'trailer': 'link',
            'year': 2010,
            'rating': 8.8,
            'genre_id': 1,
            'director_id': 1
            }

        movie = self.movie_service.create(m1)
        assert movie is not None
        assert movie.id is not None

    def test_update(self):
        m1 = {
            'id': 1,
            'title': 'Первый фильм',
            'description': 'Description',
            'trailer': 'link',
            'year': 2010,
            'rating': 8.8,
            'genre_id': 1,
            'director_id': 1
        }
        self.movie_service.update(m1)

    def test_partial_update(self):
        m1 = {
            'id': 1,
            'title': 'Новое имя'
        }
        self.movie_service.update(m1)

    def test_delete(self):
        self.movie_service.delete(1)
