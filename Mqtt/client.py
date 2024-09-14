import time
import paho.mqtt.client as mqtt
import tclab

# MQTT settings
MQTT_BROKER = 'localhost'
MQTT_PORT = 1883
TOPIC = 'test'

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print(f"Failed to connect, return code {rc}")

def publish_temperature():
    client = mqtt.Client("TCLabPublisher")
    client.on_connect = on_connect
    client.connect(MQTT_BROKER, MQTT_PORT)
    
    client.loop_start()
    
    try:
        with tclab.TCLabModel() as lab:
            print("Publishing temperatures...")
            while True:
                temp = round(lab.T1, 2)
                temp = round(lab.T2, 4)
                client.publish(TOPIC, str(temp))
                client.publish(TOPIC, str(temp))
                print(f"Published: {temp}°C")
                time.sleep(1)  # Sleep for 1 second before publishing the next reading
    except KeyboardInterrupt:
        print("Stopping temperature publishing...")
    finally:
        client.loop_stop()
        client.disconnect()

 

if __name__ == "__main__":
    publish_temperature() 
