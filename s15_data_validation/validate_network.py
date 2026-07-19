import re
import json

def is_valid_ipv4(ip_string):
    # RegEx stricte qui vérifie la structure globale X.X.X.X
    blocks = ip_string.split('.')
    if len(blocks) != 4:
        return False
    
    try:
        # Vérification mathématique de chaque octet (O-255)
        return all(0 <= int(block) <= 255 for block in blocks)
    except ValueError:
        return False # Contient des lettres ou des caractères invalides
    
def validate_config_stream(file_path):
    ip_pattern = re.compile(r'ip address\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

    with open(file_path, 'r', encoding='utf-8') as config_file:
        for line_num, line in enumerate(config_file, 1):
            match = ip_pattern.search(line)
            if match:
                extracted_ip = match.group(1)
                # Barrière de sécurité
                if is_valid_ipv4(extracted_ip):
                    yield extracted_ip, line_num
               
if __name__ == "__main__":
    # Dictionnaires pour stocker nos résultats de manière structurée
    network_report = {
        "valid_hosts": [],
        "corrupted_hosts":[]
    }
    
    print("--- STARTING SECURE EXTRACTION & JSON PARSING ---")
    
    # Lecture en flux continu (Streaming)
    for ip, line_num in validate_config_stream("dirty_router.cfg"):
        if is_valid_ipv4(ip):
            print(f"✅ Valid IP: {ip} (Line {line_num})")
            network_report["valid_hosts"].append({
                "line": line_num,
                "ip_address": ip,
                "status": "APPROVED"
            })
        else:
            print(f"🚨 ALERT: Corrupted IP: {ip} (Line {line_num})")
            network_report["corrupted_hosts"].append({
                "line": line_num,
                "ip_address": ip,
                "status": "REJECTED",
                "reason": "Octet out of bounds (>255)"
            })

# ECRITURE DU RAPPORT JSON (L'export industriel)
with open("network_report.json", "w", encoding="utf-8") as json_file:
    # indent=4 permet de rendre le fichier JSON lisible pour l'humain
    json.dump(network_report, json_file, indent=4)

print("\n💾 [SUCCESS] network_report.json generated perfectly.")