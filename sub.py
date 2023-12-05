from paho.mqtt import client as mqtt_client
import random

broker = "test.mosquitto.org"
topic = "python/mqtt_project"
port = 1883
# username = "Hp"
# password = "pcpgohd12"
client_id = f"subscribe-{random.randint(1,1000)}"


def broker_connection():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connection Succesful!")
        else:
            print("Connection Failed, reason {rc}")

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)

    return client


def subscribe(client):
    def on_message(client, userdata, msg):
        print(f"Received '{msg}' from '{msg.topic}'")

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = broker_connection()
    subscribe(client)
    client.loop_forever()


if __name__ == "__main__":
    run()
