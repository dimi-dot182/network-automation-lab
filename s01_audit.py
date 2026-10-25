import pandas as pd
import io

# 1. MOCK DATA GENERATION
# Jeu de données OSP simulé avec des erreurs (Nulls)
csv_mock = """Chambre_ID,Type,X_Coord,Y_Coord,Status
CH-001,L2T,45.3421,5.0311,Deployed
CH-002,L3T,45.3435,,Planned
CH-003,L4T,,5.0350,Deployed
CH-004,L2T,45.3450,5.0360,
CH-005,,45.3461,5.0375,Planned"""

# 2. DATA INGESTION
# Simulation d'un pd.read_csv() classique
df = pd.read_csv(io.StringIO(csv_mock))

# 3. DATAFRAME INSPECTION (Structure & Types)
print("--- DATAFRAME INFO ---")
df.info()

# 4. MISSING VALUES AUDIT (Identification des trous)
print("\n--- MISSING VALUES COUNT ---")
print(df.isnull().sum())

# 5. SPATIAL DATA CLEANSING (Purge & Fill)

# Hard Purge : Élimination des lignes sans X ou Y
df_cleaned = df.dropna(subset=['X_Coord', 'Y_Coord']).copy()

# Soft Fix : Remplacement des valeurs nulles sur les attributs métier
df_cleaned['Status'] = df_cleaned['Status'].fillna('Unknown')
df_cleaned['Type'] = df_cleaned['Type'].fillna('TBD')

print("\n--- CLEANED DATAFRAME ---")
print(df_cleaned)
print("\n--- NEW MISSING VALUES COUNT ---")
print(df_cleaned.isnull().sum())