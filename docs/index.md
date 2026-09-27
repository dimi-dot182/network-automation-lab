# 🌍 OSP Infrastructure & Spatial Data Automation
## Executive Portfolio & Applied R&D Ledger

This portfolio documents the continuous transition of physical telecommunications infrastructure (Heavy Civils, Submarine Cables, Long-Haul) into software-defined, automated data pipelines.

### 🏗️ CORE 1 : Cloud-Native Automation Engine & Data Resilience
* [2026-09-24]

The Challenge: Tier-1 infrastructure projects generate chaotic field data. Fragmented subcontractors and heterogeneous spreadsheets create Garbage In, Garbage Out (GIGO) and expose confidential financial metadata on unsecured networks.

Applied Engineering & Skills Mastered:

Zero-Touch ETL Pipeline: Engineered dynamic Multi-Sheet parsing scripts using Python (pandas, openpyxl) to normalize raw data into Relational Star Schemas via agnostic Project_ID routing.

Version Control & Data Privacy: Mastered advanced Git orchestration. Implemented strict .gitignore boundaries for Data Leak Prevention (DLP), resolved divergent repository histories, and decoupled the execution codebase (src/) from proprietary business assets (data/).

The ROI: Eradicated administrative bottlenecks and achieved absolute data compliance. Automated ingestion drastically cuts OPEX, enabling project control teams to scale deployments seamlessly.


### [CORE 3 - Spatial ETL Routing & Data Contract]: OSP Data Contract & Spatial Routing
* **[Delivered: 2026-09-27]**

**L'Enjeu (Heavy Civils) :**
L'incapacité à croiser financièrement et spatialement les impacts de Génie Civil et de Fibre Optique sur des projets majeurs (ex: BHNS, Tramways) provient de données entrantes sous format "fichier plat". Le manque d'intégrité référentielle, notamment l'absence du Host Infrastructure (propriétaire tiers), fausse l'analyse d'impact et paralyse les équipes d'ingénierie.

**La Solution (Zero-Touch Data Flow):**
Mise en place d'un Data Gatekeeper en Python. L'ETL ingère les données brutes via un système de Multi-Sheet Parsing et applique instantanément un Fail-Fast Data Contract. Les données non conformes sont rejetées. Les données valides subissent un routage spatial automatique, transformant une ligne administrative ambigüe en entités géométriques normalisées.

**Le ROI (Cost Avoidance):**
Protection totale de la base de données spatiale (PostgreSQL/PostGIS) contre les corruptions humaines. L'éradication du Garbage In supprime les temps morts d'audit manuel. Le Schedule Variance est sécurisé grâce à une fiabilité absolue des dépendances (GC validé -> FO libérée).