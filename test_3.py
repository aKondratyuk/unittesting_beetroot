import unittest
import alarms


class SystemAlerts(unittest.TestCase):

    def test_power_outage_alert(self):
        self.assertRaises(alarms.PowerError, alarms.power_outage_detected, True)

    def test_gasoline_level_warning(self):
        self.assertWarns(alarms.GasolineLevelWarning, alarms.gasoline_level_check, 150)


if __name__ == '__main__':
    unittest.main()
