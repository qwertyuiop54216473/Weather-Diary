from weather import WeatherEntry
from storage import WeatherStorage
from plotter import plot_temperature
from datetime import datetime

def input_date(prompt):
    while True:
        date_str = input(prompt)
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            print('Неверный формат даты! Введите в формате ГГГГ-ММ-ДД')

def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Должно быть число!')

def main():
    storage = WeatherStorage()
    while True:
        print("\nWeather Diary")
        print("1. Добавить запись")
        print("2. Посмотреть все записи")
        print("3. Удалить запись")
        print("4. Фильтрация")
        print("5. Построить график")
        print("0. Выход")
        choice = input("Выберите пункт: ")

        if choice == '1':
            date = input_date("Дата (ГГГГ-ММ-ДД): ")
            temp = input_float("Температура: ")
            desc = input("Описание: ")
            prec = input_float("Осадки: ")
            storage.add_entry(WeatherEntry(date, temp, desc, prec))
        elif choice == '2':
            for i, entry in enumerate(storage.entries):
                print(f"{i}: {entry.date.strftime('%Y-%m-%d')} | {entry.temperature}°C | {entry.description} | Осадки: {entry.precipitation}")
        elif choice == '3':
            i = input_float("Введите номер записи для удаления: ")
            storage.remove_entry(int(i))
        elif choice == '4':
            filter_type = input("Фильтровать по (date/temp): ")
            if filter_type == 'date':
                d = input("Введите дату (ГГГГ-ММ-ДД): ")
                result = storage.filter_by_date(d)
            else:
                mn = input_float("Минимальная температура: ")
                mx = input_float("Максимальная температура: ")
                result = storage.filter_by_temp(mn, mx)
            for entry in result:
                print(f"{entry.date.strftime('%Y-%m-%d')} | {entry.temperature}°C | {entry.description} | Осадки: {entry.precipitation}")
        elif choice == '5':
            plot_temperature(storage.entries)
        elif choice == '0':
            break

if __name__ == "__main__":
    main()
