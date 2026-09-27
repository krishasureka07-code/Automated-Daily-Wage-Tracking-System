import unittest
from src.wage_calculator import compute_daily_wage
class TestWageCalculator(unittest.TestCase):
    def test_8_hours(self):
        result = compute_daily_wage(800, 8)
        self.assertEqual(result["regular_hours"], 8)
        self.assertEqual(result["overtime_hours"], 0)
        self.assertEqual(result["regular_pay"], 800)
        self.assertEqual(result["overtime_pay"], 0)
        self.assertEqual(result["total_wage"], 800)
    def test_4_hours(self):
        result = compute_daily_wage(600, 4)
        self.assertEqual(result["regular_hours"], 4)
        self.assertEqual(result["overtime_hours"], 0)
        self.assertEqual(result["regular_pay"], 300)
        self.assertEqual(result["overtime_pay"], 0)
        self.assertEqual(result["total_wage"], 300)
    def test_overtime(self):
        result = compute_daily_wage(600, 11)
        self.assertEqual(result["regular_hours"], 8)
        self.assertEqual(result["overtime_hours"], 3)
        self.assertEqual(result["regular_pay"], 600)
        self.assertEqual(result["overtime_pay"], 337.5)
        self.assertEqual(result["total_wage"], 937.5)
    def test_negative_hours(self):
        result = compute_daily_wage(600, -2)
        self.assertEqual(result["total_wage"], 0)
if __name__ == "__main__":
    unittest.main() 
