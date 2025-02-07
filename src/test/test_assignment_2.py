import unittest
import sys
import os
import numpy as np
from scipy.interpolate import CubicSpline

# Ensure src is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.main.assignment_2 import (
    neville_interpolation, newton_forward_interpolation, hermite_interpolation, cubic_spline_interpolation
)

class TestAssignment2(unittest.TestCase):
    def test_neville_interpolation(self):
        x_vals = [3.6, 3.8, 3.9]
        y_vals = [1.675, 1.436, 1.318]
        self.assertAlmostEqual(neville_interpolation(x_vals, y_vals, 3.7), 1.555, places=2)

    def test_newton_forward_interpolation(self):
        x_vals = [7.2, 7.4, 7.5, 7.6]
        y_vals = [23.5492, 25.3913, 26.8224, 27.4589]
        self.assertAlmostEqual(newton_forward_interpolation(x_vals, y_vals, 7.3), 24.016575, places=3)

    def test_hermite_interpolation(self):
        x_vals = [3.6, 3.8, 3.9]
        y_vals = [1.675, 1.436, 1.318]
        dy_vals = [-1.195, -1.188, -1.182]
        H = hermite_interpolation(x_vals, y_vals, dy_vals)
        self.assertIsInstance(H, np.ndarray)

    def test_cubic_spline_interpolation(self):
        x_vals = [2, 5, 8, 10]
        y_vals = [3, 5, 7, 9]
        cs = cubic_spline_interpolation(x_vals, y_vals)
        self.assertAlmostEqual(cs(6), 5.6006006, places=3)

if __name__ == '__main__':
    unittest.main()
