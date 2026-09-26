import pathlib

# 1. Define the Root Directory (Ton répertoire principal)
# pathlib.Path.cwd() récupère le répertoire actuel où le script est exécuté
root_dir = pathlib.Path.cwd() / "03. Survey_Relevés_Chambre"

# 2. Define standard sub-folders for each Chamber (Les cassettes de ton boîtier)
chamber_subfolders = ["01. Formulaire", "02. Photos", "03. Autre"]

# 3. Dummy Data: List of Sites and Chambers (Ce qui viendra plus tard de ton .gpkg)
osp_data = {
    "Site_PL01": ["PL01_ORA_25_87324", "PL01_ORA_25_87325"],
    "Site_PL02": ["PL02_FR_99_11111"]
}

def create_osp_structure():
    """Generates the automated folder structure for OSP Field Data."""
    
    # Create the high-level system folders (exist_ok=True évite les crashs si le dossier existe déjà)
    (root_dir / "00. QField_Raw_Sync").mkdir(parents=True, exist_ok=True)
    (root_dir / "01. QField_Cloud_Import").mkdir(parents=True, exist_ok=True)
    
    processed_dir = root_dir / "02. OSP_Processed_Data"
    
    # Loop through the dictionary to build the granular structure
    for site, chambers in osp_data.items():
        for chamber in chambers:
            for sub in chamber_subfolders:
                target_path = processed_dir / site / chamber / sub
                target_path.mkdir(parents=True, exist_ok=True)
                print(f"Deployment successful: {target_path}")

if __name__ == "__main__":
    print("Initiating OSP Directory Build...")
    create_osp_structure()