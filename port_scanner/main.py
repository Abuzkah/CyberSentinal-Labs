import socket

def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((host, port))
        s.close()
        return True
    except:
        return False

def main():
    host = '127.0.0.1'
    ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]
    print(f"Scanning {host}...")
    for port in ports:
        status = scan_port(host, port)
        print(f"Port {port:5}: {'OPEN' if status else 'CLOSED'}")
    print("Scan complete.")

if __name__ == "__main__":
    main()
