def lagrange(x, y, x_):
    print("Многочлен Лагранжа:\n")
    n = len(x)
    result = 0.0
    terms = []
    
    for i in range(n):
        term = y[i]
        num_parts = []
        den_parts = []
        
        for j in range(n):
            if i != j:
                num_val = x_ - x[j]
                den_val = x[i] - x[j]
                term *= num_val / den_val
                num_parts.append(f"({x_:.2f}-{x[j]:.2f})")
                den_parts.append(f"({x[i]:.2f}-{x[j]:.2f})")
        
        num_str = "*".join(num_parts)
        den_str = "*".join(den_parts)
        
        result += term
        terms.append(term)
        
        print(f"Слагаемое l_{i}(x) = [{y[i]}] * [{num_str}] / [{den_str}]")
        print(f"          = {term:.6f}")
    
    print("\nL(x) = " + " + ".join([f"{t:.6f}" for t in terms]) + f" ={result:.6f}\n")
    return result
