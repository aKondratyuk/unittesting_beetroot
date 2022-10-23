import unittest
import code


class EntertainmentSystemTests(unittest.TestCase):

    # Якщо перший аргумент дає True, то тест пропускається
    @unittest.skipIf(code.regional_jet(), 'Not available on regional jets')
    def test_movie_license(self):
        daily_movie = code.get_daily_movie()
        licensed_movies = code.get_licensed_movies()
        self.assertIn(daily_movie, licensed_movies)

    # Якщо перший аргумент дає False, то тест пропускається
    @unittest.skipUnless(not code.regional_jet(), 'Not available on regional jets')
    def test_wifi_status(self):
        wifi_enabled = code.get_wifi_status()
        self.assertTrue(wifi_enabled)

    # @unittest.skip - пропускаємо тест завжди
    def test_device_temp(self):
        if code.regional_jet():
            self.skipTest('Not available on regional jets')
        temp = code.get_device_temp()
        self.assertLess(temp, 50)  # if temp > 40: raise Error

    def test_maximum_display_brightness(self):
        if code.regional_jet():
            self.skipTest('Not available on regional jets')
        brightness = code.get_maximum_display_brightness()
        # Almost до 7 знаку після коми
        self.assertAlmostEqual(brightness, 400)  # 0.1 + 0.2 == 0.3, 0.1 + 0.2 == 0.3000000000000000004


if __name__ == '__main__':
    unittest.main()
