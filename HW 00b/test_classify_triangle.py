import unittest
from classify_triangle import classify_triangle

class TestClassifyTriangle(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")
    
    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 8), "Isosceles")
        self.assertEqual(classify_triangle(8, 5, 5), "Isosceles")

    def test_scalene(self):
        self.assertEqual(classify_triangle(7, 8, 9), "Scalene")
        self.assertEqual(classify_triangle(6, 8, 10), "Scalene and Right Triangle")  


    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene and Right Triangle")
        self.assertEqual(classify_triangle(5, 12, 13), "Scalene and Right Triangle")

    def test_not_triangle(self):
        self.assertEqual(classify_triangle(1, 1, 3), "Not a Triangle")
        self.assertEqual(classify_triangle(0, 0, 0), "Not a Triangle")

if __name__ == "__main__":
    unittest.main()