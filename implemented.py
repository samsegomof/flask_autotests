from DAO.movie import MovieDAO
from DAO.director import DirectorDAO
from DAO.genre import GenreDAO
from services.director_service import DirectorService
from services.genre_service import GenreService
from services.movie_service import MovieService
from setup_db import db

movie_dao = MovieDAO(session=db.session)
director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)

movie_serv = MovieService(dao=movie_dao)
genre_serv = GenreService(dao=genre_dao)
director_serv = DirectorService(dao=director_dao)
