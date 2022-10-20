import unittest
import code


class EntertainmentSystemTests(unittest.TestCase):

    def test_movie_license(self):
        daily_movies = code.get_daily_movies()
        licensed_movies = code.get_licensed_movies()

        # Write your code below:
        for movie in daily_movies:
            print(movie)
            with self.subTest():
                self.assertIn(movie, licensed_movies)


if __name__ == "__main__":
    unittest.main()