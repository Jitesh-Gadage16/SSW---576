import unittest
from classify_triangle import classify_triangle

class TestClassifyTriangle(unittest.TestCase):

    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")

    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(5, 5, 8), "Isosceles")

    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(7, 8, 9), "Scalene")

    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene and Right Triangle")

    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(1, 1, 2), "Not a Triangle")

    def test_negative_values(self):
        self.assertEqual(classify_triangle(-3, 4, 5), "Not a Triangle")

    def test_zero_values(self):
        self.assertEqual(classify_triangle(0, 0, 0), "Not a Triangle")

if __name__ == "__main__":
    unittest.main()
