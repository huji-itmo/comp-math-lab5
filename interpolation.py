import math


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
        show_differences_table(deltas)

        if x0 >= self.x[-1]:
            t = (x0 - self.x[-1]) / h
            product = lambda i: t - i + 1
        else:
            t = (x0 - self.x[0]) / h
            product = lambda i: t - (i - 1)

        result = deltas[0][0]
        t_product = 1.0
        factorial = 1.0
        for i in range(1, self.n):
            factorial *= i
            t_product *= product(i)
            result += (t_product / factorial) * deltas[i][0]
        return result

    def _build_finite_diff_table(self):
        table = [[0.0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            table[0][i] = self.y[i]

        for k in range(1, self.n):
            for i in range(self.n - k):
                table[k][i] = table[k - 1][i + 1] - table[k - 1][i]
        return table


def show_differences_table(diff_table):
    for order in range(len(diff_table)):
        print(f"Δ^{order} |", end="")
        for value in diff_table[order]:
            if abs(value) > 1e-10:
                print(f" {str(round(value, 6)).rjust(9)}", end="")
        print()
    print()
