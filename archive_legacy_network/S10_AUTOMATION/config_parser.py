# S10 - Premier Script de Network Parsing
print("--- Début de l'analyse du fichier ---")
# 1. On ouvre le fichier en mode "r" (read / lecture)
try:
    with open("router_config.txt", "r") as file:
        lines = file.readlines() # On lit les lignes du fichier et on les stocke dans une liste
    # 2. On parcourt chaque ligne du fichier
    for line in lines:
        # On nettoie la ligne (on enlève les espaces inutiles au début et à la fin)
        clean_line = line.strip()

        # Ton nouveau bloc de détection de description
        if clean_line.startswith("description"):
            description_found = clean_line.replace("description ","") # On enlève le mot "description" pour ne garder que le texte de la description
        
            print(f"✅ SUCCÈS : Description isolée : {description_found}")

        # 3. On cherche le mot-clé "ip address"
        if clean_line.startswith("ip address"):

            # 4. On découpe la ligne pour isoler l'IP
            # .split() transforme "ip address 192.168.1.1 255.255.255.0"
            # en une liste : ["ip", "address", "192.168.1.1", "255.255.255.0"]
            parts = clean_line.split()
            ip_found = parts[2] # Le 3ème élément (index 2) est l'adresse IP
            mask_found = parts[3] # Le 4ème élément (index 3) est le masque de sous-réseau

            print(f"✅ SUCCÈS : IP isolée : {ip_found}")
            print(f"✅ SUCCÈS : Masque isolé : {mask_found}")

except FileNotFoundError:
    print("❌ ERREUR : Fichier introuvable !")

print("--- Analyse terminée ---")