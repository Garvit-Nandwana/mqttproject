import random
import json

def random_data():
    temperatures = [random.randint(5, 50) for i in range(5)]
    humidity = [random.randint(10, 100) for i in range(5)]

    data = {}
    data['Temperatures'] = temperatures
    data['Humidity'] = humidity

    return json.dumps(data)


if __name__ == "__main__":
    print(random_data())