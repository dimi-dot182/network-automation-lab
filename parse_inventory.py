import json

try: 
    with open('inventory.json', 'r') as file:
        data = json.load(file)

    print(f"Targeting Device: {data['device_name']}")
    print(f"IP Adress:{data['management_ip']}")
    print(f"Status: {data['status']}")

except json.JSONDecodeError as e:
    print(f"CRITICAL ERROR: Invalid JSON syntax in inventory.json -> {e}")