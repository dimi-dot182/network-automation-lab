## Execution: python json_reader.py

import json # <--- THIS IS THE TOOLBOX IMPORT

# 1. Open the inventory file in 'read' mode (r)
with open('inventory.json', 'r') as my_file:
    # 2. Load the content and convert it into a Python List
    devices = json.load(my_file)

print("--- [UPTIME REPORT] ---")

# 3. Filter devices that are 'up'
for devices in devices:
    if devices["status"] == "up":
        print(f"DEVICE ONLINE: {devices['hostname']} (IP: {devices['ip']})")

print("--- [END OF REPORT] ---")