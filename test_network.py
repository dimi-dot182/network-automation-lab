import requests

def test_api_robustness():
    # Nous ciblons une URL de test qui renvoie un JSON valide
    url = "https://httpbin.org/json"

    try:
        print("--- Tentative de connexion ---")
        response = requests.get(url, timeout=5)

        #1. Validation de la couche HTTP
        response.raise_for_status() # Lève une erreur si code 4xx ou 5xx

        #2. Validation du Content-Type (On veut du JSON uniquement)
        content_type = response.headers.get('Content-Type', '')
        if 'application/json' not in content_type:
            raise ValueError(f"Format invalide reçu : {content_type}")
        
        #3. Extraction et validation de la charge utile (Payload)
        data = response.json() # Peut lever une erreur si le JSON est mal formé

        if 'equipement_optique' not in data:
            raise KeyError("ERREUR CRITIQUE : La clé 'equipement_optique' est absente de l'inventaire !")
        
        print("✅ SUCCESS : Données reçues et intégrité validée !")

        if not data: #Si le dictionnaire ou la liste est vide
            raise ValueError("Le Payload reçu est vide !")
        
        print("✅ SUCCESS : Données reçues et validées avec succès !")
        print(f"Clés trouvées dans le JSON : {list(data.keys())}")

    except requests.exceptions.RequestException as e:
        print(f"❌ ERREUR RESEAU/HTTP : {e}")
    except ValueError as e:
        print(f"❌ ERREUR DE DONNÉES (Validation) : {e}")
    except KeyError as e:
        print(f"❌ ERREUR D'INTÉGRITÉ (Clé manquante) : {e}") # <-- Ajoute cette ligne

if __name__ == "__main__":
    test_api_robustness()