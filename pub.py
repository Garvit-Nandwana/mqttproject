from paho.mqtt import client as mqtt_client
import random
from data import random_data
import time

broker = "test.mosquitto.org"
port = 1883
topic = "python/mqtt_project"
#username = "Hp"
#password = "pcpgohd12"
client_id = f"publish-{random.randint(1,1000)}"


def broker_connection():
    def on_connect(rc):
        if rc == 0:
            print("Connection Successful!")
        else:
            print(f"Failed to connect, reason {rc}")

    # Setting client id
    client = mqtt_client.Client(client_id)

    client.on_connect = on_connect

    client.connect(broker, port)

    return client


def publish(client):
    message_count = 1

    while True:
        time.sleep(4)

        data = random_data()

        message = f"{message_count}. {data}"
        
        result = client.publish(topic, message)

        print(result)

        status = result[0]

        if status == 0:
            print(f"'{message}' sent to topic '{topic}'")
        else:
            print(f"Failed to sent message to topic '{topic}'")

        message_count += 1

        if message_count > 5:
            break

        

def run():
    client = broker_connection()
    client.loop_start()
    publish(client=client)
    client.loop_stop()


if __name__ == "__main__":
    run()
