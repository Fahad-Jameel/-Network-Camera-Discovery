# Network Camera Discovery Script

## Overview
This Python script facilitates the discovery of network-connected cameras within a specified IP range on a local network. The script uses the `socket` and `subprocess` modules to retrieve network information and perform a basic scan for devices with a user-defined camera name in their hostname.

## How to Use
1. Replace the `camera_name` variable in the script with the name of the camera you are searching for.
2. Run the script in a Python environment.

## Requirements
- Python 3.x
- Windows Operating System (as the script uses the `ipconfig` command specific to Windows)

## Important Notes
- Ensure that you have the necessary permissions to run this script on the target network.
- The script assumes that the camera's hostname contains the specified camera name. Adjust the condition in the script if the actual naming convention differs.

## Example
```python
# Replace the manufacturer or model name with the name of your camera
camera_name = "MyCamera"
