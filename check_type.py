# Simulating the loaded JSON data from our inventory
inventory_data = {
    "device_name": "Edge-Router-01",
    "management_ip": "192.168.1.1",
    "interfaces": [
        "GigabitEthernet1",
        "GigabitEthernet2"
    ],
    "status": "Production"
}

# Verifying the data type in Python
interfaces_data = inventory_data["interfaces"]
print(f"The data type of the 'interfaces' key is: {type(interfaces_data)}")
print(f"Is it a list? {isinstance(interfaces_data, list)}")