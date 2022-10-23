import unittest
import monitor


class Test(unittest.TestCase):

    def test_request_flight_attendant(self):
        self.assertWarns(monitor.CustomerRequestWarning, monitor.request_flight_attendant)

    def test_calculate_remaining_time(self):
        self.assertRaises(TypeError, monitor.calculate_remaining_time, " ")


if __name__ == '__main__':
    unittest.main()
