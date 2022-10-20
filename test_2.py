import unittest
import code


class EntertainmentSystemTests(unittest.TestCase):

    def test_movie_license(self):
        daily_movie = code.get_daily_movie()
        licensed_movies = code.get_licensed_movies()
        self.assertIn(daily_movie, licensed_movies)

    def test_wifi_status(self):
        wifi_enabled = code.get_wifi_status()
        self.assertTrue(wifi_enabled)

    def test_device_temp(self):
        temp = code.get_device_temp()
        self.assertLess(temp, 50)  # if temp > 40: raise Error

    def test_maximum_display_brightness(self):
        brightness = code.get_maximum_display_brightness()
        # Almost до 7 знаку після коми
        self.assertAlmostEqual(brightness, 400)  # 0.1 + 0.2 == 0.3, 0.1 + 0.2 == 0.3000000000000000004


if __name__ == '__main__':
    unittest.main()
