import sqlite3

def ingest_osp_data(project_id, name, infra_type, budget):
    conn = sqlite3.connect("osp_core.db")
    cursor = conn.cursor()
    
    try:
        # Utilisation de paramètres (?) pour prévenir les injections SQL (Standard Industriel)
        cursor.execute("""
        INSERT INTO osp_projects (Project_ID, Project_Name, Infrastructure_Type, CAPEX_Budget)
        VALUES (?, ?, ?, ?)
        """, (project_id, name, infra_type, budget))
        
        conn.commit()
        print(f"[DEPLOYMENT] Ingested: {project_id} - {name}")
        
    except sqlite3.IntegrityError as e:
        # RCA Automatisé : Le script intercepte la duplication sans crasher le pipeline
        print(f"[RCA - BLOCK] GIGO Prevented! Duplication attempt on '{project_id}'.")
        print(f"-> Root Cause Error: {e}")
        
    finally:
        conn.close()

if __name__ == "__main__":
    # 1. Ingestion initiale propre
    ingest_osp_data("TRAM-T8-001", "Tramway T8 Extension", "Heavy Civils", 1500000.0)
    
    # 2. Tentative de duplication (Simulation d'une erreur de saisie ou d'un doublon SIG)
    ingest_osp_data("TRAM-T8-001", "Tramway T8 Faux Doublon", "Relocation", 45000.0)