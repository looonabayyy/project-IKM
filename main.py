students = [
    {"last_name": "Иванов", "first_name": "Иван", "grade": 9, "day": 15, "month": 1, "year": 2007},
    {"last_name": "Петров", "first_name": "Артем", "grade": 8, "day": 2, "month": 3, "year": 2008},
    {"last_name": "Сидорова", "first_name": "Анна", "grade": 10, "day": 20, "month": 7, "year": 2006},
    {"last_name": "Кузнецов", "first_name": "Максим", "grade": 11, "day": 9, "month": 11, "year": 2005},
    {"last_name": "Смирнова", "first_name": "Екатерина", "grade": 9, "day": 30, "month": 5, "year": 2007},
    {"last_name": "Орлов", "first_name": "Даниил", "grade": 8, "day": 12, "month": 2, "year": 2008},
    {"last_name": "Волкова", "first_name": "Мария", "grade": 10, "day": 7, "month": 9, "year": 2006},
    {"last_name": "Зайцев", "first_name": "Никита", "grade": 11, "day": 18, "month": 6, "year": 2005},
    {"last_name": "Федорова", "first_name": "Ольга", "grade": 9, "day": 1, "month": 12, "year": 2007},
    {"last_name": "Морозов", "first_name": "Кирилл", "grade": 8, "day": 25, "month": 8, "year": 2008},
    {"last_name": "Алексеев", "first_name": "Илья", "grade": 9, "day": 4, "month": 4, "year": 2007},
    {"last_name": "Николаева", "first_name": "Дарья", "grade": 10, "day": 10, "month": 10, "year": 2006},
    {"last_name": "Павлов", "first_name": "Егор", "grade": 11, "day": 19, "month": 3, "year": 2005},
    {"last_name": "Романова", "first_name": "Софья", "grade": 8, "day": 22, "month": 6, "year": 2008},
    {"last_name": "Захаров", "first_name": "Алексей", "grade": 9, "day": 13, "month": 9, "year": 2007},
    {"last_name": "Ковалева", "first_name": "Полина", "grade": 10, "day": 6, "month": 1, "year": 2006},
    {"last_name": "Белов", "first_name": "Михаил", "grade": 11, "day": 28, "month": 2, "year": 2005},
    {"last_name": "Григорьева", "first_name": "Вероника", "grade": 8, "day": 16, "month": 7, "year": 2008},
    {"last_name": "Денисов", "first_name": "Андрей", "grade": 9, "day": 21, "month": 11, "year": 2007},
    {"last_name": "Мельникова", "first_name": "Алина", "grade": 10, "day": 8, "month": 5, "year": 2006},
    {"last_name": "Семенов", "first_name": "Павел", "grade": 11, "day": 14, "month": 4, "year": 2005},
    {"last_name": "Тарасова", "first_name": "Юлия", "grade": 8, "day": 3, "month": 12, "year": 2008},
    {"last_name": "Борисов", "first_name": "Роман", "grade": 9, "day": 26, "month": 6, "year": 2007},
    {"last_name": "Васильева", "first_name": "Ксения", "grade": 10, "day": 11, "month": 8, "year": 2006},
    {"last_name": "Комаров", "first_name": "Сергей", "grade": 11, "day": 5, "month": 10, "year": 2005},
]

# ---------- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ----------

def get_season(month):
    if month == 12 or month == 1 or month == 2:
        return "зима"
    elif month == 3 or month == 4 or month == 5:
        return "весна"
    elif month == 6 or month == 7 or month == 8:
        return "лето"
    else:
        return "осень"


def ins_sort(data_list, keys):
    new_list = data_list[:] 

    for i in range(1, len(new_list)):
        curr = new_list[i]
        j = i - 1

        while j >= 0:
            push = False
            for key in keys:
                if curr[key] < new_list[j][key]:
                    push = True
                    break
                elif curr[key] > new_list[j][key]:
                    break
            if push:
                new_list[j + 1] = new_list[j]
                j -= 1
            else:
                break
        new_list[j + 1] = curr
    return new_list

def print_students(student_list):
    print("-" * 60)
    for student in student_list:
        print(
            student["last_name"], student["first_name"],
            "| класс:", student["grade"],
            "| дата:", student["day"], ".", student["month"], ".", student["year"]
        )
    print("-" * 60)

# ---------- ОСНОВНЫЕ ФУНКЦИИ ----------

def show_all():
    sort = ins_sort(students, ["grade", "last_name"])
    print("\n ПОЛНЫЙ СПИСОК УЧЕНИКОВ (отсортировано по классу и фамилии):")
    print_students(sort)


def show_by_season():
    season = input("Введите сезон (зима/весна/лето/осень): ").lower()
    
    valid_seasons = ["зима", "весна", "лето", "осень"]
    if season not in valid_seasons:
        print("ОШИБКА: введите одно из значений: зима, весна, лето, осень")
        return  
    
    season_endings = {
        "зима": "зимой",
        "весна": "весной", 
        "лето": "летом",
        "осень": "осенью"
    }
    
    result = []
    for student in students:
        if get_season(student["month"]) == season:
            result.append(student)

    if len(result) == 0:
        season_with_ending = season_endings[season]
        print(f"\n Нет учеников, родившихся {season_with_ending}")
        return
    
    result = ins_sort(result, ["month", "day", "last_name"])

    season_with_ending = season_endings[season]
    print(f"\n УЧЕНИКИ, РОДИВШИЕСЯ {season_with_ending.upper()} (отсортировано по дате рождения):")
    print_students(result)

def show_by_grade():
    try:
        grade = int(input("Введите класс (8-11): "))

        if grade < 8 or grade > 11:
            print("ОШИБКА: класс должен быть от 8 до 11")
            return
    except ValueError:
        print("ОШИБКА: введите целое число")
        return
    except:
        print("ОШИБКА: неизвестная ошибка ввода")
        return

    result = []
    for stud in students:
        if stud["grade"] == grade:
            result.append(stud)
    
    if len(result) == 0:
        print(f"\n Нет учеников {grade} класса")
        return
    
    result = ins_sort(result, ["month", "day", "last_name"])
    print(f"\n УЧЕНИКИ {grade} КЛАССА (отсортировано по дате рождения):")
    print_students(result)

# ---------- МЕНЮ ----------

def main_menu():
    while True:
        print("\n" + "="*40)
        print("ʕ•ᴥ•ʔ УЧЁТ ДНЕЙ РОЖДЕНИЯ УЧЕНИКОВ ʕ•ᴥ•ʔ")
        print("="*40)
        print("1 — Показать всех учеников")
        print("2 — Показать именинников по сезону")
        print("3 — Показать учеников одного класса")
        print("0 — Выход")
        print("-"*40)

        choice = input("Ваш выбор: ")

        if choice == "1":
            show_all()
        elif choice == "2":
            show_by_season()
        elif choice == "3":
            show_by_grade()
        elif choice == "0":
            print("\nВыход из программы")
            break
        else:
            print("ОШИБКА: выберите пункт от 0 до 3")

        if choice != "0":
            input("\nНажмите Enter чтобы продолжить...")


if __name__ == "__main__":
    print("="*50)
    print("ПРОГРАММА ДЛЯ УЧЁТА ДНЕЙ РОЖДЕНИЯ УЧЕНИКОВ")
    print("="*50)
    main_menu()