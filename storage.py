import json
from weather import WeatherEntry

class WeatherStorage:
    def __init__(self, filename='weather.json'):
        self.filename = filename
        self.entries = []
        self.load()

    def add_entry(self, entry):
        self.entries.append(entry)
        self.save()

    def remove_entry(self, index):
        if 0 <= index < len(self.entries):
            self.entries.pop(index)
            self.save()

    def filter_by_date(self, date_query):
        return [e for e in self.entries if e.date.strftime('%Y-%m-%d') == date_query]

    def filter_by_temp(self, min_temp, max_temp):
        return [e for e in self.entries if min_temp <= e.temperature <= max_temp]

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump([entry.to_dict() for entry in self.entries], f, indent=2)

    def load(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.entries = [WeatherEntry.from_dict(d) for d in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.entries = []
