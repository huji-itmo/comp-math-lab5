import math
from typing import Callable


class Interpolator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)

    def lagrange(self, x0):
        result = 0.0
        for i in range(self.n):
            term = self.y[i]
            for j in range(self.n):
                if i != j:
                    term *= (x0 - self.x[j]) / (self.x[i] - self.x[j])
            result += term
        return result

    def show_table_if_can(self):
        if self._is_finite_diff():
            deltas = self._build_finite_diff_table()
            self.show_differences_table(deltas)

    def newton(self, x0):
        if self._is_finite_diff():
            return self._newton_finite_diff(x0)
        else:
            return self._newton_divided_diff(x0)

    def _is_finite_diff(self, eps=1e-4):
        for i in range(self.n - 2):
            diff1 = self.x[i + 1] - self.x[i]
            diff2 = self.x[i + 2] - self.x[i + 1]
            if abs(diff1 - diff2) > eps:
                return False
        return True

    def _newton_divided_diff(self, x0):
        table = [[0.0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            table[0][i] = self.y[i]

        for level in range(1, self.n):
            for i in range(self.n - level):
                table[level][i] = (table[level - 1][i + 1] - table[level - 1][i]) / (
                    self.x[i + level] - self.x[i]
                )

        coef = [table[level][0] for level in range(self.n)]
        result = coef[0]
        product = 1.0
        for i in range(1, self.n):
            product *= x0 - self.x[i - 1]
            result += coef[i] * product
        return result

    def _newton_finite_diff(self, x0):
        deltas = self._build_finite_diff_table()
        h = self.x[1] - self.x[0]

        if x0 > (self.x[0] + self.x[-1]) / 2:
            # интерполяция назад
            t = (x0 - self.x[-1]) / h

            result = deltas[-1][0]  # Initial term from the last row of the first column
            product = 1.0
            factorial = 1.0
            for j in range(1, self.n):  # j is the order of the difference
                factorial *= j
                product *= t + j - 1  # t(t+1)(t+2)... for backward
                result += (product / factorial) * deltas[self.n - j - 1][j]
                # Access last row of column j
        else:
            # интерполяция вперед

            t = (x0 - self.x[0]) / h
            result = deltas[0][0]  # Start with the first element of the first column
            product = 1.0
            factorial = 1.0
            for j in range(1, self.n):
                factorial *= j
                product *= t - (j - 1)
                # Access the j-th column of the first row for forward coefficients
                result += (product / factorial) * deltas[0][j]

        return result

    def _build_finite_diff_table(self):
        n = len(self.x)
        diff_table = [[0] * n for _ in range(n)]
        for i in range(n):
            diff_table[i][0] = self.y[i]
        for j in range(1, n):
            for i in range(n - j):
                diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]
        return diff_table

    def show_differences_table(self, diff_table):
        n = len(self.x)
        print("\nТаблица конечных разностей:")
        print("x".ljust(10), end="")
        for i in range(n):
            print(f"Δ^{i}y".ljust(15), end="")
        print()
        for i in range(n):
            print(f"{self.x[i]:<10.4f}", end="")
            for j in range(n - i):
                print(f"{diff_table[i][j]:<15.6f}", end="")
            print()
