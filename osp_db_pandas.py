import sqlite3
import pandas as pd

def analyze_osp_pipeline(db_name="osp_core.db"):
    # 1. Ouverture de la connexion
    conn = sqlite3.connect(db_name)
    
    # 2. Requête SQL d'extraction (Read)
    query = "SELECT * FROM osp_projects"
    
    # 3. Data Ingestion : SQL -> Pandas DataFrame
    # C'est ici que la magie opère. Pandas transforme la table SQL en objet analytique.
    df = pd.read_sql_query(query, conn)
    
    conn.close()
    
    print("\n[ETL SUCCESS] SQLite DB loaded into Pandas DataFrame.")
    print("-" * 50)
    print(df)
    print("-" * 50)
    
    # Démonstration de la puissance d'analyse Pandas :
    total_capex = df['CAPEX_Budget'].sum()
    print(f"\n-> TOTAL ACTIVE CAPEX EXPOSURE : {total_capex:,.2f} EUR")

if __name__ == "__main__":
    analyze_osp_pipeline()