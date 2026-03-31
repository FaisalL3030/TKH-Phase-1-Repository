import socket

# Define your targets
targets = ["127.0.0.1", "8.8.8.8", "1.1.1.1", "10.0.0.1"]

for ip in targets:
    print(f"--- Checking Server: {ip} ---")
    
    # Create the 'knocker' (Socket)
    # AF_INET = IPv4, SOCK_STREAM = TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Don't wait more than 1 second for a response
    s.settimeout(1)
    
    # connect_ex returns 0 if successful (port open)
    result = s.connect_ex((ip, 22))
    
    if result == 0:
        print(f"SUCCESS: Port 22 is OPEN on {ip}")
    else:
        print(f"FAILED: Port 22 is CLOSED on {ip}")
    
    # Always close the door when finished
    s.close()
