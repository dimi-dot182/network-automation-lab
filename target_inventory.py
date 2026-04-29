# Network Inventory Simultation
devices = [
    {"hostname": "CORE-SW-01", "ip": "10.0.0.1", "role": "Core"},
    {"hostname": "DIST-SW-01", "ip": "10.0.0.10", "role": "Distrib"},
    {"hostname": "ACCESS-SW-01", "ip": "10.0.0.100", "role": "Access"},
    {"hostname": "ROUTEUR-SW-01", "ip": "10.0.0.110", "role": "Routeur"}
]

print("--- [NETWORK ARCHITECT AUDIT] ---")
for device in devices:
    print(f"DEVICE: {device['hostname']} | IP: {device['ip']} | TYPE: {device['role']}")

print("-" * 35)
print(f"Total devices scanned: {len(devices)}")