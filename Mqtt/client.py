import time
import paho.mqtt.client as mqtt
import tclab

# MQTT settings
MQTT_BROKER = 'localhost'
MQTT_PORT = 1883
TOPIC = 'test'

def publish_temperature():
    client = mqtt.Client("TCLabPublisher", callback_api_version=5)  # Added callback_api_version argument
    client.connect(MQTT_BROKER, MQTT_PORT)
    
    client.loop_start()
    
    try:
        with tclab.TCLabModel() as lab:
            print("Publishing temperatures...")
            while True:
                temp = round(lab.T1, 2)
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
