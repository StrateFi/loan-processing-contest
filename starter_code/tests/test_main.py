import unittest
from starter_code.main import determine_bank

class TestDetermineBank(unittest.TestCase):
    def test_bank_a(self):
        application_data = {
            "credit_score": 720,
            "loan_amount": 50000,
            "business_type": "retail"
        }
        self.assertEqual(determine_bank(application_data), "Bank A")

    def test_bank_b(self):
        application_data = {
            "credit_score": 650,
            "loan_amount": 75000,
            "business_type": "manufacturing"
        }
        self.assertEqual(determine_bank(application_data), "Bank B")

    def test_bank_c(self):
        application_data = {
            "credit_score": 800,
            "loan_amount": 100000,
            "business_type": "technology"
        }
        self.assertEqual(determine_bank(application_data), "Bank C")

if __name__ == "__main__":
    unittest.main()
