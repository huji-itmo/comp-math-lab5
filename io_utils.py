import math


def get_user_points():
    num_points = int(input("Введите число точек: "))
    x_data = []
    y_data = []
    for idx in range(num_points):
        x_data.append(float(input(f"Координата X точки {idx}: ")))
        y_data.append(float(input(f"Координата Y точки {idx}: ")))
    return x_data, y_data


def load_file_data():
    file_path = input("Укажите путь к файлу данных: ")
    x_vals = []
    y_vals = []
    with open(file_path) as data_file:
        for data_line in data_file:
            values = data_line.strip().split()
            if len(values) > 1:
                x_vals.append(float(values[0]))
                y_vals.append(float(values[1]))
    return x_vals, y_vals


def create_function_points():
    function_options = {
        1: lambda val: math.sin(val),
        2: lambda val: math.cos(val),
    }

    print("Доступные функции:\n1. Синус\n2. Косинус")
    choice = int(input("Ваш выбор: "))
    selected_func = function_options.get(choice)
    if not selected_func:
        raise RuntimeError("Неизвестная функция")

    left_bound = float(input("Начало интервала: "))
    right_bound = float(input("Конец интервала: "))
    if right_bound <= left_bound:
        raise ValueError("Некорректные границы интервала")

    point_count = int(input("Число точек для генерации: "))
    step_size = (right_bound - left_bound) / point_count
    x_coords = []
    y_coords = []
    current_x = left_bound
    for _ in range(point_count):
        x_coords.append(current_x)
        y_coords.append(selected_func(current_x))
        current_x += step_size
    return x_coords, y_coords


def print_xy_table(x_vals, y_vals):
    print("|    X      |    Y      |")
    print("-" * 25)
    for i in range(len(x_vals)):
        print(
            f"| {str(round(x_vals[i], 4)).center(10)} | {str(round(y_vals[i], 4)).center(10)} |"
        )
    print()
