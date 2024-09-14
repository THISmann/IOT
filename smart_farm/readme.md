Smart Farm Distributed system

**Architecture de Système Distribué**

1. **Dispositifs IoT (capteurs et caméras)**
2. **Serveur MQTT Local sur Raspberry Pi**
3. **Cloud Centralisé (Infrastructure Cloud)**
4. **Pipeline de Traitement de Données et d'IA**
5. **Base de Données**
6. **Système d’Alerte en Temps Réel**
7. **API pour Accès aux Données**
8. **Tableau de Bord**

---

### **Exigences Fonctionnelles**

1. **Collecte de Données Multi-source** : Le système doit pouvoir collecter des données de capteurs (température, humidité, qualité du sol, etc.) et des images toutes les heures depuis des milliers de dispositifs.
2. **Transmission des Données au Cloud** : Chaque Raspberry Pi doit transférer les données collectées vers le cloud centralisé toutes les heures pour analyse et stockage.
3. **Traitement des Données avec IA** : Un service cloud doit exécuter des algorithmes d'IA pour analyser les données et les images, et extraire les informations utiles comme les anomalies ou les maladies des plantes.
4. **Système d'Alerte en Temps Réel** : Si une condition anormale est détectée (par exemple une maladie), une alerte doit être envoyée aux fermes concernées pour qu'elles puissent réagir rapidement.
5. **Tableau de Bord et API** : Fournir un tableau de bord centralisé pour les utilisateurs et une API RESTful open-source pour accéder aux données depuis n'importe où dans le monde.

---

### **Exigences Non Fonctionnelles**

1. **Scalabilité** : Le système doit être capable de gérer plus de 1000 dispositifs IoT avec la possibilité d'augmenter facilement la capacité à mesure que le nombre de dispositifs augmente.
2. **Faible Latence pour les Alertes** : Les alertes doivent être transmises en temps réel ou presque instantanément lorsqu’une condition critique est détectée.
3. **Résilience et Tolérance aux Pannes** : Le système doit continuer à fonctionner même en cas de pannes locales sur certains dispositifs IoT ou dans certaines régions. Utilisation de zones de disponibilité multiples dans le cloud pour assurer une haute disponibilité.
4. **Sécurité** : Les données transmises entre les dispositifs IoT, le cloud et les utilisateurs doivent être sécurisées par des méthodes comme TLS (Transport Layer Security). Les accès aux API doivent être gérés par des clés d’API ou des systèmes d’authentification robustes (OAuth, JWT).
5. **Stockage Efficace** : Les images et les données agricoles collectées doivent être stockées efficacement pour minimiser les coûts de stockage, tout en restant accessibles pour les analyses futures.
6. **Maintenance Facile et Surveillance** : Le système doit être facile à maintenir, avec des capacités de surveillance centralisée pour identifier rapidement les problèmes dans le réseau IoT ou dans les services cloud.


### **1. Device Layer Services (IoT Edge Services)**

These services are located on the **IoT devices** (Raspberry Pi) and handle communication between the sensors, cameras, and the central cloud infrastructure.

#### 1.1 **MQTT Broker Service (Edge)**

#### 1.2 **Data Aggregation Service**

#### 1.3 **Camera Service**

#### 1.4 **Local Alert Service**

### **2. Cloud Communication and Upload Services**

These services facilitate the secure upload of sensor data and images from the Raspberry Pi to the cloud infrastructure.

#### 2.1 **MQTT Bridge Service (Cloud)**

#### 2.2 **Batch Data Upload Service**

- **Role**: Uploads data and images from the Raspberry Pi to the cloud in regular intervals (every hour).
- **Micro-service function**: Ensures periodic uploads, compresses data and images, and securely transmits the information via HTTPS or MQTT to the cloud.

### **3. Cloud Processing and Storage Services**

These services are responsible for ingesting, processing, analyzing, and storing the data and images uploaded by the Raspberry Pi devices.

#### 3.1 **Data Ingestion Service**

- **Role**: Handles incoming sensor data from the IoT devices and stores it in a cloud database for processing and storage.
- **Micro-service function**: Uses a message queue (e.g., **Apache Kafka** or **AWS Kinesis**) to handle incoming data streams, ensuring no data is lost during high traffic.

#### 3.2 **Image Storage Service**

#### 3.3 **Data Processing & AI Analysis Service**

#### 3.4 **Anomaly Detection & Alerting Service**

#### 3.5 **Data Storage Service**

### **4. Cloud-to-Device Communication Services**

These services allow real-time communication from the cloud to the IoT devices for sending alerts or commands.

#### 4.1 **Real-Time Command Service**

#### 4.2 **Alert Notification Service**

### **5. Management and Monitoring Services**

These services ensure the entire IoT ecosystem is running efficiently, and that system performance is monitored continuously.

#### 5.1 **Device Management Service**

#### 5.2 **Monitoring & Logging Service**

#### 5.3 **Scaling & Load Balancing Service**

### **6. User Interface and API Services**

These services provide access to the data and system functionalities through dashboards and APIs.

#### 6.1 **API Gateway Service**

#### 6.2 **Dashboard & Visualization Service**


---

### **Summary of Services and Their Roles:**

- **Edge Services (on Raspberry Pi)**: Collect, process, and temporarily store data locally, handle MQTT communication, and manage local actions like alerts or actuators.
- **Cloud Services**: Ingest, process, analyze, and store data from multiple devices globally, and manage real-time alerts or commands.
- **AI and Data Processing Services**: Use machine learning models to analyze sensor data and images, detect anomalies, and trigger appropriate responses.
- **API and Dashboard Services**: Provide external access to data and offer visualization tools for real-time monitoring and control of the system.
- **Device and System Management Services**: Ensure the fleet of devices is healthy, up-to-date, and functioning properly, with monitoring and scaling capabilities for the cloud infrastructure.

 ![1726313418080](image/readme/1726313418080.png)


etc....
