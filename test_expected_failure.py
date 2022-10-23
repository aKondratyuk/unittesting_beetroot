import unittest
import code


class CustomerFeedbackTests(unittest.TestCase):

    @unittest.expectedFailure
    def test_survey_form(self):
        self.assertEqual(code.issue_survey(), 'Success')

    def test_complaint_form(self):
        self.assertEqual(code.log_customer_complaint(), 'Success')


if __name__ == '__main__':
    unittest.main()
