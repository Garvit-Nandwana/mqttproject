from paho.mqtt import client as mqtt_client
import random

broker = "test.mosquitto.org"
port = 1883
topic = "python/mqtt_project"
#username = "Hp"
#password = "pcpgohd12"
client_id = f"mqttproject-{random.randint(1,1000)}"


def broker_connection():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connection Successful!")
        else:
            print(f"Failed to connect, reason {rc}")

    # Setting client id
    client = mqtt_client.Client(client_id)

    client.on_connect = on_connect

    client.connect(broker=broker, port=port)

    return client




