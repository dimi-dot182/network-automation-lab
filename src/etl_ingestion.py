# ====================================================
# CORE 1 - SESSION [Date] : MULTI-SHEET PARSING
# ====================================================
# [Ton ancien code de parsing ici]

import pandas as pd
import os

# 1. THE MASTER MAPPING DICTIONARY (Corrigé selon règles OSP)
COLUMN_MAPPING = {
    # Keys
    "N°REF": "Affaire_Ref",
    "ID / U": "Affaire_Ref",
    "Projet": "Project_ID",
    "programme": "Project_ID",
    "Nom Affaire": "Project_ID",
    
    # Éclatement des identifiants (Correction métier)
    "acteurs CDT": "Field_Manager_ID",
    "Conducteur de Travaux": "Field_Manager_ID",
    "CDP": "Client_PM_ID",

    # Financials
    "N° Devis": "Quote_Number",
    "numéro_de_devis": "Quote_Number",
    "montant_devis": "Quote_Amount",
    "Montant Devis HT": "Quote_Amount",
    "N° Commande": "PO_Number",
    "N°Commande SFR": "PO_Number",
    "Montant BDC HT": "PO_Amount",
    "Montant Facturé HT": "Invoiced_Amount",

    # Civils & Cables (Éclatement métier)
    "INFRA": "Network_Owner",         # Ex: SFR, CPTL
    "type_opération": "Civil_Task",   # Ex: Tranchée, Chambre
    "GC": "Civil_Task",
    "date_debut": "Date_Debut_GC",
    "date_demolition_ancienne_infra": "Date_Demolition",
    "nbr_cables": "Cable_Count",
    "liste_des_cables": "Cable_List",
    "date_debut_intervention": "Intervention_Start",
    "date_fin_intervention": "Intervention_End",
    "date_limite_réalisation (OPC)": "Target_Completion_Date",
    "Date Livraison Prévue": "Target_Completion_Date"
}

def ingest_multisheet_excel(filepath):
    """Pipeline ETL avec Data Cleansing et Coalesce conditionnel."""
    if not os.path.exists(filepath):
        print(f"⚠️ Fichier introuvable : {filepath}")
        return

    print(f"📂 Ouverture du classeur : {os.path.basename(filepath)}")
    
    try:
        excel_app = pd.ExcelFile(filepath, engine='openpyxl')
        sheets = excel_app.sheet_names

        for sheet in sheets:
            print(f"\n--- 🔄 Traitement de l'onglet : [{sheet}] ---")
            df = pd.read_excel(excel_app, sheet_name=sheet)
            
            # 1. EXTRACT : Normalisation des colonnes
            df_normalized = df.rename(columns=COLUMN_MAPPING)
            
            matched_keys = [col for col in df_normalized.columns if col in COLUMN_MAPPING.values()]
            print(f"🔍 Clés actives : {matched_keys[:7]}")

            # 2. TRANSFORM : The Coalesce Logic (Data Cleansing)
            # Si Target_Completion_Date existe mais a des trous, on tente de les boucher avec Date_Debut_GC
            if 'Target_Completion_Date' in df_normalized.columns and 'Date_Debut_GC' in df_normalized.columns:
                # Pandas COALESCE : fillna()
                df_normalized['Target_Completion_Date'] = df_normalized['Target_Completion_Date'].fillna(df_normalized['Date_Debut_GC'])
                print("⚡ COALESCE appliqué : Dates cibles manquantes remplies par la date de début GC.")

            # On pourrait injecter ici df_normalized vers PostgreSQL

    except Exception as e:
        print(f"🚨 CRITICAL ERROR sur {filepath}")
        print(f"Détail : {e}\n")

if __name__ == "__main__":
    target_workbook = "ODAL 2026.09.11 - Exemple de Colonne sur Tableau de suivi.xlsx"
    ingest_multisheet_excel(target_workbook)

# ====================================================
# CORE 3 - SESSION [Date] : OSP DATA CONTRACT & ROUTING
# ====================================================
# [Le bloc de vérification HOST_INFRASTRUCTURE ici]

import pandas as pd
import numpy as np

# 1. INGESTION (Création de la variable df - La ligne ne doit PAS être commentée)
# Remplace "NOM_DE_L_ONGLET_MERIGNAC" par le nom exact écrit sur l'onglet dans Sheets/Excel
df = pd.read_excel("data/ODAL 2026.09.11 - Exemple de Colonne sur Tableau de suivi.xlsx", 
    sheet_name="Modèle Suivi DEV GC + FO Mérign")

# 2. DATA CONTRACT (Vérification de df)
target_col = 'HOST_INFRASTRUCTURE'

if target_col not in df.columns:
    raise KeyError(f"CRITICAL GIGO ALERT: The column '{target_col}' is missing from the source file. Pipeline halted.")

mask_active_gc = (df['GC'].notna()) & (df['GC'].astype(str).str.strip().str.upper() != 'NA')
invalid_rows = df[mask_active_gc & df[target_col].isna()]

if not invalid_rows.empty:
    error_msg = f"DATA CORRUPTION: {len(invalid_rows)} active GC interventions are missing a '{target_col}'. Fix the source Excel file."
    raise ValueError(error_msg)

print("Data Contract Validated. Proceeding to GC/FO Split...")

# 3. SPATIAL ROUTING & NORMALIZATION (Le Split)
print("Initiating Spatial Routing...")

# Route A : Flux Génie Civil (GC)
mask_gc = (df['GC'].notna()) & (df['GC'].astype(str).str.strip().str.upper() != 'NA')
df_gc = df[mask_gc].copy()
df_gc['TYPE_RESEAU'] = 'GC' # Standardisation forcée

# Route B : Flux Fibre Optique (FO / Optique)
mask_fo = (df['Optique'].notna()) & (df['Optique'].astype(str).str.strip().str.upper() != 'NA')
df_fo = df[mask_fo].copy()
df_fo['TYPE_RESEAU'] = 'FO' # Standardisation forcée

print(f"Routing System Check: {len(df_gc)} entités GC isolées, {len(df_fo)} entités FO isolées.")