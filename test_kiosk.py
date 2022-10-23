import unittest
import kiosk


class CheckInKioskTests(unittest.TestCase):

    def setUp(self):
        print("I'm executing before test")
        
    def tearDown(self):
        print("I'm after test")

    # setUpClass - виконується лише один раз перед запуском функцій, що будуть тестуватись
    @classmethod
    def setUpClass(cls):
        kiosk.power_on_kiosk()

    def test_check_in_with_flight_number(self):
        print('Testing the check-in process based on flight number')

    def test_check_in_with_passport(self):
        print('Testing the check-in process based on passport')

    # tearDownClass - виконується в кінці виконання усіх тестів.
    @classmethod
    def tearDownClass(cls):
        kiosk.power_off_kiosk()

    # Наприклад, ми користуємось базою даних чи якимось файлом, або девайсом
    # Тоді нам необхідно перед тестуванням функцій підключитись до бази, відкрити файл чи
    # включили девайс, тоді на допомогу прийде:
    # @classmethod
    # def setUpClass(cls):
    # Виконає включення один раз і все.
    # Після того як ми виконали тестування девайсу, бази даних, файлу. То нам необхідно
    # все повимикати, від'єднатись чи закрити файл. Тоді на допомогу прийде:
    # @classmethod
    # def tearDownClass(cls):
    # Виконується лише один раз. Після того як усі тести завершені.
    # !!! Усі назви [setUpClass, tearDownClass] - вбудовані для unittest. Так само як слово test_


if __name__ == '__main__':
    unittest.main()
