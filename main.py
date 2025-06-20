import numpy as np
import math 
from methods.newtonWithFiniteDif import newtonWithFiniteDifferences
from methods.newtonWithDivDif import newtonWithDividedDifferences
from methods.lagrange import lagrange
import time

def readData():
    print("каким образом вводим данные?")
    print("(file/console/function)")
    while True:
        print("ответ принимается в формате (fi/c/fu)")
        inp = input()   
        inp = inp.lower()
        if inp == "c" or inp == "fi" or inp == "fu":
            break
        print("неверный ввод")

    if inp == "c":
        return readFromConsole()
    elif inp == "fi":
        return readFromFile()
    else:
        return readFromFunction()

def readFromFunction():
    func_arr = {1: func1, 2: func2}

    print("Выберите функцию из предложенных:")
    print("1) exp(x)")
    print("2) x + 2x^2")
    f_numb = input()
    try:
        f_numb = int(f_numb)
    except: 
        print("ожидалось число")
        readData()
        return
    if f_numb != 1 and f_numb !=2 : 
        print("ожидалось числа 1 или 2")
        readData()
        return
    func = func_arr.get(f_numb)
    print(f_numb)
    a = float(input("Введите левую границу интервала: "))
    b = float(input("Введите правую границу интервала: "))
    n = int(input("Введите количество точек на интервале: "))
    x_ = float(input("Введите значение аргумента: "))
    h = (b - a) / (n - 1)
    x = []
    y = []

    for i in range(0, n):
        x.append(a + i * h)
        y.append(func(x[i]))
    return np.array(x),np.array(y),x_

def func1(x):
    return math.exp(x)

def func2(x):
    return x + 2 * x ** 2

def readFromConsole():
    print("Введите значения x через пробел:")
    x = np.array(list(map(float, input().split())))
    print("Введите значения y через пробел:")
    y = np.array(list(map(float, input().split())))
    print("Введите значение x_:")
    x_ = input().strip()
    return x, y, x_

def dispatchToConsole():
    print("Возникла ошибка, желаете ввести данные с консоли?")
    while True:
        print("(y/n)")
        inp = input()   
        inp = inp.lower()
        if inp == "y" or inp == "n":
            break
        print("неверный ввод")
    if inp == "y":
        return readFromConsole() 
    print("программа завершается")
    time.sleep(2)
    exit()

def readFromFile():
    try:
        with open("input.txt", "r") as file:
            lines = file.readlines()  
            
            if len(lines) < 3:
                print("Ошибка: файл должен содержать 3 строки")
                return dispatchToConsole()
            
            x = np.array(list(map(float, lines[0].split())))
            y = np.array(list(map(float, lines[1].split())))
            
            x__str = lines[2].strip()
            
            if not x__str:
                print("Ошибка: третья строка пустая")
                return dispatchToConsole()
                
            
            try:
                x_ = float(x__str)
            except ValueError:
                print("Ошибка: в третьей строке должно быть одно число")
                return dispatchToConsole()
    
    except FileNotFoundError:
        print("Файл input.txt не найден")
        return dispatchToConsole()
    except (ValueError, TypeError):
        print("Ошибка формата данных: ожидались числа в первых двух строках")
        return dispatchToConsole()
    except Exception as e:
        print(f"Ошибка при чтении файла: {str(e)}")
        return dispatchToConsole()
    
    if len(x) != len(y) or len(x) == 0:
        print("Ошибка: массивы x и y разной длины или пустые")
        return dispatchToConsole()
    return x, y, x_

def isDividedDifferences(X) -> bool:
    if len(X) < 2:
        print("Для проверки нужно как минимум 2 узла")
        return False
    
    base_step = X[1] - X[0]
    
    for i in range(1, len(X) - 1):
        current_step = X[i + 1] - X[i]
        if not (abs(current_step - base_step) < 1e-6 * max(1.0, abs(base_step))):
            print(f"узлы не равноотстоящие")
            return False
    
    print(f"Узлы равноотстоящие с шагом {base_step:.2f}")
    return True

def main():
    x,y,x_ = readData()
    newtonOut = 0
    if isDividedDifferences(x):
        newtonOut = newtonWithFiniteDifferences(x,y,x_)
    else:
        newtonOut = newtonWithDividedDifferences(x,y,x_)

    lagrangeOut = lagrange(x,y,x_)

    print("--------------------------------------------------------------------------\n")
    print("Результаты:")
    print(f"Лагранж: {lagrangeOut}")
    print(f"Ньютон: {newtonOut}")

if __name__ == "__main__":
    main()

