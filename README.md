# IoT Home Automation and Security System

## Abstract

In today's fast-paced world, individuals often struggle to balance their professional and household responsibilities. This project aims to simplify household chores and enhance security by proposing a system that automates specific tasks and safeguards the home against intruders.

The proposed system allows users to remotely control devices using a dedicated mobile app, communicating with the system through the HTTP protocol. This interaction requires both the mobile device and the system to be connected to the same WLAN.

Additionally, a Passive Infrared (PIR) sensor enhances security. If an intruder is detected, the PIR sensor notifies the system, which, in turn, alerts the user through the mobile app and their Gmail account.

## Introduction

The project involves a Raspberry Pi 4 Model B, a circuit with LEDs on a breadboard, and a smartphone app. The Raspberry Pi controls the circuit via GPIO pins, and an HTTP server on the Pi serves wireless requests from the smartphone. The circuit comprises 4 LEDs and 1 PIR sensor.

The mobile app features various buttons, each generating distinct HTTP requests. These requests instruct the HTTP server to perform specific actions. The app communicates the Raspberry Pi's intended actions when buttons are pressed.

The "Enable Security" button activates the PIR sensor. If motion is detected, the Raspberry Pi activates the 4th LED and sends an email alert to the user, including the intrusion time and date. The "Disable Security" button turns off the 4th LED.

## Hardware and Software Requirements

### Hardware Requirements
- Raspberry Pi 4 Model B (2GB RAM)
- Smartphone
- PIR Sensor
- LEDs
- Breadboard
- Jumper Wires
- Micro SD Card
- Multi-Format Card Reader
- Ethernet Cable

### Software Requirements
- PuTTy
- Raspberry Pi Imager
- VNC Viewer
- Kodular App Inventor
- Android OS
- Raspbian OS
- Python

### Block Diagram
![Block Diagram](https://github.com/saptajitbanerjee/Remote-Home-Monitoring-and-Control/blob/main/Block%20Diagram.png)

### Flow Diagram
![Flow Diagram](https://github.com/saptajitbanerjee/Remote-Home-Monitoring-and-Control/blob/main/Flow%20Diagram.png)

### Photo of the Circuit
![Photo of the circuit](https://github.com/saptajitbanerjee/Remote-Home-Monitoring-and-Control/blob/main/Circuit%202.png)

## Results and Discussion

- Users can wirelessly control and communicate with the system through the mobile app.
- The mobile app allows remote switching of devices within the circuit.
- System status can be monitored through emails sent to the user's Gmail account, triggered by the Raspberry Pi.
### App
![App Screen](https://github.com/saptajitbanerjee/Remote-Home-Monitoring-and-Control/blob/main/App%202.png)
![Code Blocks](https://github.com/saptajitbanerjee/Remote-Home-Monitoring-and-Control/blob/main/App%203.png)

[Watch the Project Demo](https://github.com/saptajitbanerjee/Remote-Home-Monitoring-and-Control/blob/main/IoT-1/RHMC%20Project.mp4)

## Conclusion

The efficiency of the HTTP protocol in IoT applications, such as Home Automation, is evident in this project. Implementing the HTTP protocol requires an active HTTP server in the IoT system's controller service.

For successful communication, devices in the IoT system and user devices must send HTTP requests to the controller device, each request containing the controller device's IPv4 address.

The SMTP protocol is employed for system status notifications, sent to users via email.

In cases where WiFi is unavailable, communication remains possible by connecting user smartphones to the IoT system's controller device through Mobile Hotspot or Bluetooth.
