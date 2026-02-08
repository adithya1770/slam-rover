# SLAM Rover Project

This project implements a small autonomous buggy capable of line following and basic 3D mapping. The system combines an ESP32-based control unit with a Jetson Nano for depth processing using a Kinect v1 camera. The goal was to explore how a low-cost platform can perform perception and mapping while keeping motion control simple and reliable.

## System Overview

The rover is divided into two main units:

**Control Unit (ESP32)**
- Reads IR sensors to detect the path  
- Drives DC motors through a motor driver  
- Handles real-time movement logic  
- Operates independently of the Jetson for reliability

**Perception Unit (Jetson Nano)**
- Captures RGB-D frames from Kinect v1  
- Processes depth images to generate point clouds  
- Stores frames for offline reconstruction  
- Visualizes the generated 3D scene

## Development Highlights

- A two-sensor line following approach was used for stable motion  
- Depth frames were collected while the rover moved along the path  
- Open3D was used to convert frames into point clouds  
- Initial trials with full SLAM stacks were heavy for Jetson Nano, so a lightweight pipeline was adopted  
- Power system was designed with a buck converter to supply 5V to servos and ESP32 while motors used a separate line

## Software Stack

- Python with OpenCV and Open3D on Jetson  
- libfreenect for Kinect data streaming  
- ESP32 firmware written in Arduino environment  
- Simple custom scripts for frame capture and reconstruction

## Results

- The rover successfully followed marked paths using IR sensors  
- RGB-D data was captured during motion  
- Point clouds of indoor scenes were generated and visualized  
- System demonstrated separation of real-time control and perception workloads

## Limitations Observed

- Jetson Nano memory restricts heavy SLAM frameworks  
- Kinect v1 requires good lighting and stable power  
- No wheel odometry was used, so mapping relied only on camera data

## Future Scope

- Add encoder-based odometry for better localization  
- Integrate a lighter SLAM method  
- Improve chassis stability and power distribution  
- Move toward ROS-based architecture

## References

Implementation and experiments were carried out using open-source tools such as OpenCV, Open3D, and libfreenect along with standard ESP32 development frameworks.
