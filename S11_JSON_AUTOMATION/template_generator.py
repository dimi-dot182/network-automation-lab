import json

print("--- Début de la génération de confirguration ---")

try: 
    #Etape 1 : Ouvrir et lire le fichier JSON de manière propre
    with open("router_data.json", "r") as file:
        router_data = json.load(file) # On charge le contenu du fichier JSON dans une variable Python (un dictionnaire)

    
    print(f"✅ Données JSON chargées avec succès pour le routeur : {router_data['hostname']}")
    
    #Etape 2 : Création du bloc de configuration Cisco brute via les F-Strings
    # Les triple guillemets ''' permettent d'écrire sur plusieurs lignes d'un cou
    cisco_config = f'''hostname {router_data['hostname']}
!
interface {router_data['interface']}
    description {router_data['description']}
    ip address {router_data['ip_address']} {router_data['subnet_mask']}
    no shutdown
!
end
'''
    
    #Etape 3 : Ecriture du fichier de configuration final (.txt)
    # Mode "w" pour write (écrire / écraser le fichier)
    with open("cisco_delivery.txt", "w") as delivery_file:
        delivery_file.write(cisco_config) # On écrit le bloc de configuration dans le fichier de livraison
    
    print("✅ SUCCES : Fichier 'cisco_delivery.txt' généré et prêt pour le déploiement !")
    
except FileNotFoundError:
    print("❌ ERREUR : Le fichier 'router_data.json' est introuvable !")
except json.JSONDecodeError:
    print("❌ ERREUR : Erreur de syntaxe dans le fichier JSON !")

print("--- Fin du script ---")