def divided_differences(x, y):
    n = len(x)
    table = [y.copy()]
    print("Многочлен ньютона с разделёнными разностями:\n")
    
    first_order = []
    for j in range(n-1):
        num = table[0][j+1] - table[0][j]
        den = x[j+1] - x[j]
        value = num / den
        first_order.append(value)
        print(f"f(x_{j}, x_{j+1}) = (f(x_{j+1}) - f(x_{j}))/(x_{j+1} - x_{j}) = "
              f"({table[0][j+1]:.3f} - {table[0][j]:.3f})/({x[j+1]:.3f} - {x[j]:.3f}) = {value:.3f}")
    table.append(first_order)
    
    for i in range(2, n):
        current = []
        for j in range(n - i):
            num = table[i-1][j+1] - table[i-1][j]
            den = x[j+i] - x[j]
            value = num / den
            current.append(value)
            print(f"f(x_{j},...,x_{j+i}) = (f(x_{j+1},...,x_{j+i}) - f(x_{j},...,x_{j+i-1}))/(x_{j+i} - x_{j}) = "
                  f"({table[i-1][j+1]:.3f} - {table[i-1][j]:.3f})/({x[j+i]:.3f} - {x[j]:.3f}) = {value:.3f}")
        table.append(current)
    return table

def newtonWithDividedDifferences(x, y, x_):
    table = divided_differences(x, y)
    n = len(x)
    res = table[0][0]
    mn = 1
    terms = [f"{res:.3f}"]
    products = ["1"]
    values = [res]
    
    print("\nВычисление значения в точке x =", f"{x_:.3f}")
    for i in range(1, n):
        mn *= (x_ - x[i-1])
        term = table[i][0] * mn
        res += term
        
        prod_expr = "*".join([f"({x_:.3f} - {x[k]:.3f})" for k in range(i)])
        terms.append(f"{table[i][0]:.3f} * {prod_expr}")
        products.append(f"{mn:.3f}")
        values.append(term)
    
    print("Интерполяционный многочлен Ньютона:\n")
    print(f"N_{n-1}(x) = " + " + ".join(terms) + f" = {res:.5f}\n")
    
    print(f"Результат: y({x_:.3f}) ≈ {res:.5f}")
    return res