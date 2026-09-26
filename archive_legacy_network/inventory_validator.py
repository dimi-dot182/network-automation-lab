# Simulation d'un inventaire OSP (Format JSON/Dictionnaire)
network_inventory = [
    {"device_id": "NRO-LYON-01", "type": "OLT", "status": "active"},
    {"device_id": "PM-BEAUREPAIRE-02", "type": "Splitter"}, # Il manque la clé 'status' ici !
    {"device_id": "PBO-VILLEURBANNE-05", "type": "Point de Branchement", "status": "down"},
    {"type":"PBO-VIENNE-01", "status": "up"} # Il manque la clé 'device_id' ici, mais nous allons ignorer cette erreur pour l'instant}
]

# PHASE 1 : Initialisation du compteur
error_count = 0

print("--- Début de la vérification de l'inventaire ---")

for device in network_inventory:
    try:
        # On tente de récupérer les infos
        d_id = device['device_id']
        d_status = device['status']
        print(f"Equipement {d_id} : Statut = {d_status}")

        # Tentative d'affichage du statut de chaque équipement
        print(f"Equipement {device['device_id']} : Statut = {device['status']}")

    except KeyError as e:
        
        # PHASE 2 : Incrémentation du compteur d'erreurs
        error_count += 1

        # On utilise .get() pour éviter une nouvelle KeyError si 'device_id' est aussi manquant
        unknown_id = device.get('device_id', "ID_INCONNU")
        missing_key = e.args[0] # Récupère le nom de la clé manquante
        print(f"ERREUR : Clé '{missing_key}' manquante pour l'équipement {unknown_id} !")

        # PHASE 3 : Application d'un Default Value (Unknown)
        status_fallback = "Unknown"

print("--- Vérification terminée ---")
# PHASE 4 : Bilan final (Summary)
print(f"Nombre total d'anomalies détectées : {error_count}")