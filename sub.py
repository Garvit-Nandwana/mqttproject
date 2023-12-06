from paho.mqtt import client as mqtt_client
import random
import time

broker = "test.mosquitto.org"
topic = "python/mqtt_project"
port = 1883
# username = "Hp"
# password = "pcpgohd12"
client_id = f"subscribe-{random.randint(1,1000)}"


def broker_connection():
    def on_connect(rc):
        if rc == 0:
            print("Connection Successful!")
        else:
            print("Connection Failed, reason {rc}")

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)

    return client

    
def subscribe(client):
    message_count = 1
    
    while True:
        time.sleep(5)

        def on_message(msg):
            print(f"Received '{msg.payload.decode()}' from '{msg.topic}' topic")

        client.subscribe(topic)
        client.on_message = on_message
    
        message_count += 1

        if message_count > 5:
            break

def run():
    client = broker_connection()
    client.loop_start()
    subscribe(client)
    client.loop_stop()


if __name__ == "__main__":
    run()
