import unittest
import code


class NearestExitTest(unittest.TestCase):

    def test_row_1(self):
        self.assertEqual(code.get_nearest_exit(1), 'front', 'The nearest exit to row 1 is in the front!')

    def test_row_20(self):
        self.assertEqual(code.get_nearest_exit(20), 'middle', 'The nearest exit to row 20 is in the middle!')

    def test_row_40(self):
        self.assertEqual(code.get_nearest_exit(40), 'back', 'The nearest exit to row 40 is in the back!')


if __name__ == '__main__':
    unittest.main()
