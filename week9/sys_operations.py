import os
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
print(socket.getdefaulttimeout())
print("===================")

print("Get the current Operating System Type")
print(os.name)
print("Get the current operating system name: ")
print(platform.system())

print("===================")
print("Current Process ID: ")
print(os.getpid())

file_name = "fdpractice.txt"
print(f"\n[Before Forking] Process {os.getpid()} ")

file_handle = os.open(file_name, os.O_RDWR | os.O_CREAT)
print(f"\n[Process {os.getpid()} Opened file_handle: {file_handle} ")

file_object_TextIO = os.fdopen(file_handle, "w+")

file_object_TextIO = os.write("Some string blah blah")
