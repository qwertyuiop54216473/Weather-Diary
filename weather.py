from datetime import datetime

class WeatherEntry:
    def __init__(self, date, temperature, description, precipitation):
        self.date = date  # datetime object
        self.temperature = temperature  # float
        self.description = description  # str
        self.precipitation = precipitation  # float

    @staticmethod
    def from_dict(data):
        return WeatherEntry(
            datetime.strptime(data['date'], '%Y-%m-%d'),
            float(data['temperature']),
            data['description'],
            float(data['precipitation'])
        )

    def to_dict(self):
        return {
            'date': self.date.strftime('%Y-%m-%d'),
            'temperature': self.temperature,
            'description': self.description,
            'precipitation': self.precipitation
        }

# Пример наследования
class RainyWeatherEntry(WeatherEntry):
    def __init__(self, date, temperature, description, precipitation, rain_intensity):
        super().__init__(date, temperature, description, precipitation)
        self.rain_intensity = rain_intensity

    def to_dict(self):
        base = super().to_dict()
        base['rain_intensity'] = self.rain_intensity
        return base

    @staticmethod
    def from_dict(data):
        base = WeatherEntry.from_dict(data)
        return RainyWeatherEntry(
            base.date, base.temperature, base.description, base.precipitation,
            data.get('rain_intensity', 'moderate')
        )
