from interpolation import Interpolator
from io_utils import (
    create_function_points,
    get_user_points,
    load_file_data,
    print_xy_table,
)
from plot import plot_function


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
                x, y, func = create_function_points()
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
    print(f"Результат методом Лагранжа: {res_lagrange}")

    interpolator.show_table_if_can()

    res_newton = interpolator.newton(x0)
    method_name = (
        "Ньютона (равноотстоящие)"
        if interpolator._is_finite_diff()
        else "Ньютона (разделённые)"
    )
    print(f"Результат методом {method_name}: {res_newton}")

    print("\nРазличия между методами:")
    print(f"| Lagrange - Newton | = {abs(res_lagrange - res_newton)}")

    plot_function(
        interpolator.x, interpolator.y, interpolator.lagrange, x0, "lagrange.pdf"
    )

    plot_function(interpolator.x, interpolator.y, interpolator.newton, x0, "newton.pdf")

    if func is not None:
        print(f"| Lagrange - f(x_0) | = {abs(res_lagrange - func(x0))}", end="")
        if abs(res_lagrange) > 1e-6:
            print(f" {abs((res_lagrange - func(x0)) / res_lagrange) * 100}%")

        print(f"| Newton - f(x_0) | = {abs(res_newton - func(x0))}", end="")
        if abs(res_newton) > 1e-6:
            print(f" {abs((res_newton - func(x0)) / res_newton) * 100}%")


if __name__ == "__main__":
    main()
