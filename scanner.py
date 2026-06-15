import socket

target = "scanme.nmap.org"

try:
    ip = socket.gethostbyname(target)
    print("Target IP:", ip)

except:
    print("Unable to resolve host")
