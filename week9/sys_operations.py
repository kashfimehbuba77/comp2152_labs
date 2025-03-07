import platform
import socket

print("Current Machine Type: ")
print(platform.machine())
print("===================")

print("Current Processor Type: ")
print(platform.architecture())
print("===================")

print("Set Socket Time Out to 50 Seconds")
print(socket.setdefaulttimeout(50))
print("Get the current Socket Time")
print(socket.getdefaulttimeout(50))

print("===================")