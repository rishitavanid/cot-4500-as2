import numpy as np
from scipy.interpolate import CubicSpline


# 1. Neville’s Interpolation
def neville_interpolation(x_vals, y_vals, x):
    n = len(x_vals)
    P = np.zeros((n, n))
    for i in range(n):
        P[i][0] = y_vals[i]
    for j in range(1, n):
        for i in range(n - j):
            P[i][j] = ((x - x_vals[i + j]) * P[i][j - 1] + (x_vals[i] - x) * P[i + 1][j - 1]) / (
                        x_vals[i] - x_vals[i + j])
    return P[0][n - 1]


# 2. Newton’s Forward Difference Table
def newton_forward_table(x_vals, y_vals):
    n = len(x_vals)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y_vals
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = (diff_table[i + 1][j - 1] - diff_table[i][j - 1]) / (x_vals[i + j] - x_vals[i])
    return diff_table


# 3. Newton’s Forward Interpolation
def newton_forward_interpolation(x_vals, y_vals, x):
    diff_table = newton_forward_table(x_vals, y_vals)
    n = len(x_vals)

    result = diff_table[0, 0]
    term = 1

    for i in range(1, n):
        term *= (x - x_vals[i - 1])
        result += term * diff_table[0, i]

    return result


# 4. Hermite Interpolation
def hermite_interpolation(x_vals, y_vals, dy_vals):
    n = len(x_vals) * 2
    H = np.zeros((n, n))
    z = np.zeros(n)
    for i in range(len(x_vals)):
        z[2 * i] = z[2 * i + 1] = x_vals[i]
        H[2 * i][0] = H[2 * i + 1][0] = y_vals[i]
    for i in range(len(x_vals)):
        H[2 * i + 1][1] = dy_vals[i]
        if i > 0:
            H[2 * i][1] = (H[2 * i][0] - H[2 * i - 1][0]) / (z[2 * i] - z[2 * i - 1])
    for j in range(2, n):
        for i in range(n - j):
            H[i][j] = (H[i + 1][j - 1] - H[i][j - 1]) / (z[i + j] - z[i])
    return H


# 5. Cubic Spline Interpolation
def cubic_spline_interpolation(x_vals, y_vals):
    cs = CubicSpline(x_vals, y_vals, bc_type='natural')
    return cs


# Main execution
if __name__ == "__main__":
    # Neville’s method
    x_vals_1 = [3.6, 3.8, 3.9]
    y_vals_1 = [1.675, 1.436, 1.318]
    print(f"Neville's Interpolation f(3.7): {neville_interpolation(x_vals_1, y_vals_1, 3.7):.6f}")

    # Newton’s Forward Interpolation
    x_vals_2 = [7.2, 7.4, 7.5, 7.6]
    y_vals_2 = [23.5492, 25.3913, 26.8224, 27.4589]
    print(f"Newton's Forward Interpolation f(7.3): {newton_forward_interpolation(x_vals_2, y_vals_2, 7.3):.6f}")

    # Hermite Interpolation
    x_vals_3 = [3.6, 3.8, 3.9]
    y_vals_3 = [1.675, 1.436, 1.318]
    dy_vals_3 = [-1.195, -1.188, -1.182]
    hermite_table = hermite_interpolation(x_vals_3, y_vals_3, dy_vals_3)
    print("Hermite Interpolation Table:")
    print(hermite_table)

    # Cubic Spline Interpolation
    x_vals_4 = [2, 5, 8, 10]
    y_vals_4 = [3, 5, 7, 9]
    cs = cubic_spline_interpolation(x_vals_4, y_vals_4)
    print(f"Cubic Spline Interpolation: f(6) ≈ {cs(6):.6f}")
