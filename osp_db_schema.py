import sqlite3

def initialize_osp_db(db_name="osp_core.db"):
    # Initialisation de la connexion à la base de données
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # DDL (Data Definition Language) : Création de la table maîtresse OSP
    # Project_ID est la PRIMARY KEY stricte. Aucune duplication tolérée.
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS osp_projects (
        Project_ID TEXT PRIMARY KEY,
        Project_Name TEXT NOT NULL,
        Infrastructure_Type TEXT NOT NULL,
        Status TEXT DEFAULT 'Planned',
        CAPEX_Budget REAL
    )
    """)

    conn.commit()
    conn.close()
    print(f"[SUCCESS] Database '{db_name}' initialized. STRICT PRIMARY KEY enforced on Project_ID.")

if __name__ == "__main__":
    initialize_osp_db()