import socket
import subprocess

# Replace the manufacturer or model name with the name of your camera
camera_name = "MyCamera"

# Get the IP address range of the local network
ipconfig = subprocess.Popen(["ipconfig"], stdout=subprocess.PIPE)
output = ipconfig.communicate()[0].decode("utf-8")
ip_address = output[output.index("IPv4 Address"):].split("\n")[0].split(": ")[1]
subnet_mask = output[output.index("Subnet Mask"):].split("\n")[0].split(": ")[1]
network_address = ".".join(ip_address.split(".")[:3]) + ".0"
ip_range = network_address + "/24"

# Scan the IP addresses in the network range for the camera device
for i in range(1, 255):
    ip = network_address + "." + str(i)
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        if camera_name.lower() in hostname.lower():
            print("Found camera device at IP address:", ip)
    except socket.herror:
        pass
