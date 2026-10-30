import json
import os
import math


# Сохранение записи
def save_expenses(expenses):
    try:
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(expenses, file, ensure_ascii=False, indent=4)
    except OSError:
        print("Ошибка: Не удалось сохранить файл data.json")

# Загрузка записи
def load_expenses():
    try:
        if os.path.exists("data.json"):

            with open("data.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, list):
                return []

            for expense in data:
                if not isinstance(expense, dict):
                    return []
                elif not ("id" in expense and "description" in expense and "amount" in expense):
                    return []

                elif not isinstance(expense['description'], str):
                    return []
                elif expense['description'].strip() == "":
                    return []
                elif type(expense['amount']) not in (int, float):
                    return []

                elif type(expense['id']) is not int or expense['id'] <= 0:
                    print('У тебя тут не правильное ID в json')
                    return []

                elif not math.isfinite(expense['amount']) or expense['amount'] <= 0:
                    print('У тебя сумма расхода ноль или меньше!')
                    return []


            ids = [expense['id'] for expense in data]
            new_ids = set(ids)
            if len(new_ids) != len(ids):
                print("У тебя тут совпадают значения")

                expenses_by_id = {}
                for expense in data:
                    expenses_by_id[expense['id']] = expense

                data = list(expenses_by_id.values())
                save_expenses(data)

            return data


        else:
            return []

    except OSError:
        print("Ошибка: Не удалось прочитать файл data.json")
        return []

    except json.JSONDecodeError:
        return []






def add_expense(description, amount):
    if expenses:
        exp_id = max(exp["id"] for exp in expenses) + 1
    else:
        exp_id = 1
    expenses.append(
        {
            "id": exp_id,
            "description": description,
            "amount": amount
        }
    )
    save_expenses(expenses)
    return expenses



def total_expense():
    total = 0
    if not expenses:
        print('Список расходов Пуст!')
    else:
        for expense in expenses:
            total = total + expense['amount']
        print(f"Общая сумма расходов: {total}$\n")
    return total



def list_expenses():
    if not expenses:
        print('Список расходов пуст!')
    for expense in expenses:
        print(f"Id: {expense['id']} | Описание: {expense['description']} | Сумма: {expense['amount']}$")



def delete_expense(expense_id):
    old_exp = len(expenses)
    exp = [exps for exps in expenses if exps["id"] != expense_id]
    expenses[:] = exp
    if len(exp) < old_exp:
        save_expenses(exp)
        return True
    else:
        return False


def menu():
    inp = 0
    while True:

        print(f"\n1.Добавить расход")
        print(f"2.Показать расходы")
        print(f"3.Показать общую сумму")
        print(f"4.Удалить расход")
        print(f"5.Выйти из прогрммы\n")


        try:
            inp = int(input("Выбери нужный варинат: "))
        except ValueError:
            print('Вы ничего не ввели, попробуйте еще раз!')
            continue

        if inp == 1:
            while True:
                description = input(f"Введите описание расхода: ").strip()

                if not description:
                    print("Ошибка: Описание не может быть пустым")
                    continue

                while True:
                    try:
                        amount = float(input("Введите сумму расхода: "))
                    except ValueError:
                        print("Ошибка: Введите число, например 12.5")
                        continue

                    if not math.isfinite(amount) or amount <= 0:
                        print("Ошибка: Сумма должна быть больше нуля")
                        continue

                    break


                add_expense(description, amount)
                print(f"Расход '{description}' на сумму {amount}$ добавлен!\n")
                break

        elif inp == 2:
            list_expenses()

        elif inp == 3:
            total_expense()

        elif inp == 4:
            list_expenses()
            try:
                expense_id = int(input(f"\nВведите номер ID расхода на удаление: "))
            except ValueError:
                print("Ошибка: Введите целое число!")
                continue

            if expense_id <= 0:
                print(f"Ошибка: ID расхода не может быть меньше 1!")
            elif delete_expense(expense_id):
                print(f"Расход с ID {expense_id} удалён!")
            else:
                print(f"Расход с ID {expense_id} не найден!")


        elif inp == 5:
            print(f"Выход из программы")
            break
        else:
            print("Ошибка: Неизвестная команда!\n")
    return True


expenses = load_expenses()
menu()

