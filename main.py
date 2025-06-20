from interpolation import Interpolator
from io_utils import (
    create_function_points,
    get_user_points,
    load_file_data,
    print_xy_table,
)


def main():
    while True:
        try:
            print(
                "Выберите способ ввода точек:\n"
                "1 - Файл\n"
                "2 - Ручной ввод\n"
                "3 - Сгенерировать из функции"
            )
            choice = int(input(""))

            if choice == 1:
                x, y = load_file_data()
            elif choice == 2:
                x, y = get_user_points()
            elif choice == 3:
                x, y = create_function_points()
            else:
                raise ValueError("Неверный выбор")

            print("\nПолучен следующий ввод:")
            print_xy_table(x, y)
            break
        except Exception as e:
            print(f"Ошибка: {e}\n")

    interpolator = Interpolator(x, y)
    x0 = float(input("Введите x0: "))

    res_lagrange = interpolator.lagrange(x0)
    print(f"Результат методом Лагранжа: {round(res_lagrange, 6)}")

    res_newton = interpolator.newton(x0)
    method_name = (
        "Ньютона (равноотстоящие)"
        if interpolator._is_finite_diff()
        else "Ньютона (разделённые)"
    )
    print(f"Результат методом {method_name}: {round(res_newton, 6)}")

    print("\nРазличия между методами:")
    print(f"| Lagrange - Newton | = {round(abs(res_lagrange - res_newton), 6)}")


if __name__ == "__main__":
    main()
