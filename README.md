# Overview

Video stream is a simple tool that lets you stream video from one device to another!

# Installation

1. Navigate to the project directory:

   `cd path/to/project`
3. Install dependecies:

   `pip install -r requirements.txt`

# How to Use

1. Start the server:
   
   For Windows:
   
     `python server.py`
   
   For Linux/MacOS:
   
     `python3 server.py`
2. Copy the IP address displayed in the console.
3. Open `client.py` and replace `SERVER IP ADDRESS` with the copied IP.
4. Run the client on another device:

   For Windows:
   
     `python client.py`
   
   For Linux/MacOS:
   
     `python3 client.py`
5. Done! You can now stream video from your webcam.

# Notes

- The server must be running before starting the client.
- Both devices must be in the same network.
  
