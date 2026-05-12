# cisco_builders.py

def generate_banner(motd_text):
    """Génère la configuration de la bannière Cisco."""
    return f"banner motd ^{motd_text}^"

def generate_interface(int_name, ip_address, mask):
    """Génère la configuration d'une interface standard."""
    return f"interface {int_name}\n description MPLS_BACKBONE\n ip address {ip_address} {mask}\n no shutdown"

# Bloc de test isolé (Battle Testing local)
if __name__ == "__main__":
    print("--- [TEST MODULE INTERNE] ---")
    test_cli = generate_interface("GigabitEthernet0/1", "192.168.1.1", "255.255.255.0")
    print(test_cli)