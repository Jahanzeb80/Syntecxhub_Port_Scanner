import socket
import threading
import logging
from datetime import datetime
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[
        logging.FileHandler("scan_results.log"),
        logging.StreamHandler() ])
def scan_port(host, port, open_ports):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.5)
            result = s.connect_ex((host, port))
            if result == 0:
                logging.info(f"[+] Port {port:5}: OPEN")
                open_ports.append(port)
    except Exception:
        pass
def run_scanner(host, ports):
    print(f"\nScanning Host: {host}")
    print(f"Time Started: {datetime.now()}\n")
    
    threads = []
    open_ports = []

    for port in ports:
        t = threading.Thread(target=scan_port, args=(host, port, open_ports))
        threads.append(t)
        t.start()

        if len(threads) >= 100:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

    print(f"Scan Finished. Open Ports: {sorted(open_ports)}")

if __name__ == "__main__":
    try:
        target = input("Target IP or Domain: ")
        target_ip = socket.gethostbyname(target)
        
        port_input = input("Enter port (e.g., 80) or range (e.g., 20-80): ")
        
        if "-" in port_input:
            parts = port_input.split("-")
            start = int(parts[0])
            end = int(parts[1])
            ports_to_scan = range(start, end + 1)
        else:
            ports_to_scan = [int(port_input)]

        run_scanner(target_ip, ports_to_scan)

    except socket.gaierror:
        print("\n[!] Could not resolve hostname.")
    except (ValueError, IndexError):
        print("\n[!] Invalid input. Use '80' or '20-80'.")
    except KeyboardInterrupt:
        print("\n[!] Scan stopped by user.")
