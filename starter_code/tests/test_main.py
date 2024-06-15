import unittest
from starter_code.main import determine_bank, extract_financial_metrics_from_pdf

class TestDetermineBank(unittest.TestCase):
    def test_bank_a(self):
        application_data = {
            "credit_score": 720,
            "loan_amount": 50000,
            "business_type": "retail",
            "cash_flow": 100000,
            "net_income": 25000,
            "DCR": 1.5,
            "gross_profit": 50000,
            "total_income_loss": 20000
        }
        self.assertEqual(determine_bank(application_data), "Bank A")

    def test_bank_b(self):
        application_data = {
            "credit_score": 650,
            "loan_amount": 75000,
            "business_type": "manufacturing",
            "cash_flow": 120000,
            "net_income": 30000,
            "DCR": 1.8,
            "gross_profit": 60000,
            "total_income_loss": 25000
        }
        self.assertEqual(determine_bank(application_data), "Bank B")

    def test_pdf_extraction(self):
        # Test PDF extraction logic
        pdf_path = "path_to_sample_pdf.pdf"
        metrics = extract_financial_metrics_from_pdf(pdf_path)
        self.assertIn("cash_flow", metrics)
        self.assertIn("net_income", metrics)

if __name__ == "__main__":
    unittest.main()
