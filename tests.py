from datetime import datetime
from weather import WeatherEntry
from storage import WeatherStorage

def run_tests():
    # Позитивные
    ws = WeatherStorage('test_weather.json')
    ws.entries = []  # start from scratch
    e1 = WeatherEntry(datetime(2024, 6, 1), 22.5, "Солнечно", 0.0)
    ws.add_entry(e1)
    assert ws.entries[0].temperature == 22.5

    # Граничные случаи
    e2 = WeatherEntry(datetime(2024, 6, 2), -50, "Холодно", 5.0)
    ws.add_entry(e2)
    assert ws.entries[1].temperature == -50

    # Негативные: удаление несуществующего индекса
    ws.remove_entry(5)  # не должно падать

    print("Все тесты пройдены!")

if __name__ == "__main__":
    run_tests()
