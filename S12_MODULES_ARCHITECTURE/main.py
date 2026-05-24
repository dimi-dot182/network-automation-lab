# main.py
import cisco_builders # On importe notre boîte à outils

# Données de production simulées (bientôt remplacées par ton JSON global)
router_config = {
    "interface": "GigabitEthernet0/0",
    "ip": "10.0.0.1",
    "mask": "255.255.255.0",
    "motd": "ACCES STRICTEMENT RESERVE AUX ARCHITECTES"
}

print("--- Lancement de l'Orcheetrateur Principal ---")

# Appel des fonctions via le namespace du module
banner_cli = cisco_builders.generate_banner(router_config["motd"])
int_cli = cisco_builders.generate_interface(
    router_config["interface"],
    router_config["ip"],
    router_config["mask"]
)

print(banner_cli)
print(int_cli)