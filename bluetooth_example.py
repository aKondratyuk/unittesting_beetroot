import unittest


# Імітація кнопки увімкнення/вимкнення
def power_cycle_device():
    print("Power cycling bluetooth device...")


class BluetoothDeviceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        power_cycle_device()

    def test_feature_a(self):
        print('Testing Feature A')

    def test_feature_b(self):
        print('Testing Feature B')

    @classmethod
    def tearDownClass(cls):
        power_cycle_device()