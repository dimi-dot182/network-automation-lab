import re
def stream_clean_config(file_path):
    # Expressions régulières compilées pour optimiser les cycles CPU
    ip_pattern = re.compile(r'ip address (\d{1,3}\. \d{1,3}\. \d{1,3}\. \d{1,3})')
    
    # Lecture ligne par ligne (Streaming) : Emprise mémoire = Proche de zéro
    with open(file_path, 'r', encoding='utf-8') as config_file:
        for line in config_file:
            match = ip_pattern.search(line)
            if match:
                yield match.group(1) # Renvoie l'IP sans bloquer le script

# Simulation de l'éxécution
if __name__ == "__main__":
    # Crée un faux fichier de config pour le test
    with open("cisco_router.cfg", "w") as f:
        f.write("interface GigabitEthernet0/1\n")
        f.write(" ip address 192.168.1.1\n")
        f.write("interface TenGigabitEthernet0/2\n")
        f.write(" ip address 10.0.0.254\n")
    
    print("--- EXTRACTED IPs (Green Coding Mode) ---")
    for ip in stream_clean_config("cisco_router.cfg"):
        print(f"Target IP found: {ip}")