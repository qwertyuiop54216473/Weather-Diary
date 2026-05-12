import matplotlib.pyplot as plt

def plot_temperature(entries):
    if not entries:
        print("Нет данных для построения графика.")
        return
    dates = [e.date for e in entries]
    temps = [e.temperature for e in entries]

    plt.figure(figsize=(10,5))
    plt.plot(dates, temps, marker='o')
    plt.title('Температура по дням')
    plt.xlabel('Дата')
    plt.ylabel('Температура, °C')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
