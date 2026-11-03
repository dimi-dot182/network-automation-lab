# 🏗️ OSP Infrastructure & Spatial Data Automation Lab

Welcome to my production-ready repository dedicated to Outside Plant (OSP) engineering, Heavy Civils project controls, and spatial data pipelines. This repository serves as a live ledger of enterprise-grade ETL data normalization and GIS automation, transitioning complex multi-project field data into scalable, zero-touch architectures.

## 🛠️ Technical Stack & Environment
* **OS:** English Enterprise Environment (Production Standards)
* **Language:** Python 3.12+ (Pandas, openpyxl, PyQGIS)
* **Database & Routing:** PostgreSQL / PostGIS (Spatial Data Normalization)
* **Version Control:** Git / GitHub (Advanced branching, Data Leak Prevention)
* **Target Architectures:** Zero-Touch ETL Pipelines, Agnostic Spatial Databases, Executive Dashboards (Looker Studio)

## 🚀 Core Architecture Sessions Ledger

### 🏗️ CORE 1 : Cloud-Native Automation Engine (Data Pipeline & ETL)
* **[2026-09-24] S02 - Version Control Resilience & Data Privacy :** Implemented strict `.gitignore` boundaries for OSP Multi-Sheet agency files, isolating `src/` from `data/` to prevent Data Breaches and unblock deployment pipelines.
* **[2026-09-20] S01 - OSP ETL Data Normalization MVP :** Validated dynamic `.xlsx` parsing using Pandas and openpyxl. Engineered a `COLUMN_MAPPING` dictionary with `fillna` mechanisms to route distinct OSP domain entities (Tramway T8, LGV33) into strict Star Schema keys, eradicating GIGO.

### 🚜 CORE 3 : Scalable Heavy Infrastructure
* **[2026-08-15] S18 - MOOVEO Spatial ETL & Data Decoupling :** Architected a decoupled spatial data flow to handle heavy utility relocations. Integrated geographic constraints with infrastructure project schedules to anticipate physical clashes and reduce schedule variance.

### 📊 CORE 4 : Executive Authority & Financial Controls
* **[2026-08-15] S18 - Power Query & Business Intelligence :** Bridged spatial constraints from the MOOVEO ETL with financial datasets via Power Query. Automated the ingestion of multi-source trackers to feed executive dashboards, driving Cost Avoidance on complex OSP deployments.

### CORE 3: Spatial ETL Routing & Data Contract
* **[2026-09-27]**

**Business Problem**: Regional agencies supply unnormalized, multi-tenant flat files (Excel) mixing Heavy Civils (GC) and Fiber Optic (FO) assets. Injecting these directly into a GIS causes spatial integrity failures, resulting in corrupted project variance reports.

**Tech Stack**: Python 3.12, Pandas, Git.

**Core Logic**:

*Fail-Fast Data Contract:* Implemented strict inbound validation requiring the HOST_INFRASTRUCTURE field for any active civil works. Pipeline halts actively via ValueError if GIGO criteria are met.

*Spatial Routing Engine:* Deconstructs hybrid tabular rows and normalizes them into distinct df_gc and df_fo dataframes, prepping the topology for LineString (Civils) and Polygon (Impact Zones) spatial joins.

**Command Ledger (Execution):**

python src/etl_ingestion.py
#Output triggers validation: "Routing System Check: X GC isolated, Y FO isolated."

### [CORE 1 Zero-Touch ETL & Fail-Fast UI Architecture]
* **[Delivered : 2026-10-02]**

**Business Problem:** Field data collection in Heavy Civil and OSP (Outside Plant) environments suffers from high "Garbage In" rates due to poor UI constraints, manual data entry errors, and disconnected photo management. This leads to severe Schedule Variances and administrative overhead during As-Built documentation.
Tech Stack: QGIS, QField, SQLite (GeoPackage), Python 3.12 (shutil, sqlite3, re), Regex.
Core Logic:

**Frontend (Fail-Fast UI):** Implementation of Drag & Drop Designer in QGIS with SQL-driven Conditional Visibility (Kill-Switch) and Regex constraints to physically block invalid data entry at the source.

**Backend (Zero-Touch ETL):** Python batch processing script that extracts QField zip returns, queries the SQLite GeoPackage as the Single Source of Truth, sanitizes Windows file paths, and routes only validated photographic evidence to the final production folder.
Command Ledger (Production-Ready): (See Document A for full SQL/Python syntax ledgers).

### 🏗️ CORE 1 : Pandas OSP Data Ingestion & Auditing
- **[Delivered: 2026-10-25]**

**[FR] L'Enjeu :** L'ingestion aveugle de données terrain (QField/DOE) incomplètes provoque un effet GIGO (Garbage In, Garbage Out) qui fait crasher les bases de données spatiales et ralentit les livrables d'ingénierie.
**[EN] The Challenge:** Blind ingestion of incomplete field data (QField/As-Builts) triggers a GIGO effect, crashing spatial databases and delaying engineering deliverables.

**[FR] La Solution (Zero-Touch Data Flow) :** Implémentation d'un script d'audit Python/Pandas effectuant une purge stricte (Hard Purge) des assets sans coordonnées X/Y et une normalisation (Soft Fix) des métadonnées, sécurisant l'intégrité avant l'export PostGIS/QGIS.
**[EN] The Solution (Zero-Touch Data Flow):** Implemented a Python/Pandas auditing script performing a 'Hard Purge' of assets lacking X/Y coordinates and a 'Soft Fix' for metadata, securing data integrity prior to PostGIS/QGIS export.

**[FR] Le ROI (Cost Avoidance & Schedule Variance) :** Élimination totale des heures de QA/QC manuelles en bureau d'études. Sécurisation des plannings d'intégration spatiale.
**[EN] The ROI (Cost Avoidance & Schedule Variance):** Total elimination of manual QA/QC hours in the design office. Bulletproof spatial integration schedules.

### 🏗️ CORE-3 SPATIAL DATA AUTOMATION : Automated Clash Detection & Dynamic PDF Layout Engine (Tramway T8)
- **[Delivered: 2026-10-28]**

#### 1. ENTERPRISE MISSION & SCENARIO
- **[FR]** Extraction et agrégation des volumes de câbles OSP (FTTH, Backbone) impactés par l'emprise des travaux du Tramway T8 pour estimer le CAPEX de dévoiement.
- **[EN]** Extraction and aggregation of impacted OSP cable volumes (FTTH, Backbone) within the Tramway T8 construction ROW to estimate relocation CAPEX.

#### 2. THE BOTTLENECK
- **[FR]** Les manipulations manuelles (GIGO) génèrent des erreurs de métrés (câbles fantômes) et la mise en page manuelle QGIS engendre un Schedule Variance massif.
- **[EN]** Manual GIS manipulation (GIGO) generates ghost cables, and manual layout drafting causes massive Schedule Variance per revision.

#### 3. THE AUTOMATED SOLUTION
- **[FR]** Création d'un pipeline PyQGIS couplé à Pandas pour extraire les géométries, calculer les pourcentages par type de réseau, et générer un Master Plan PDF à dimensionnement dynamique (A3/A0, Portrait/Paysage) de manière 100% Zero-Touch.
- **[EN]** PyQGIS pipeline coupled with Pandas to extract geometries, aggregate percentages by network type, and output a dynamically sized Master Plan PDF (A3/A0, Portrait/Landscape) using a 100% Zero-Touch workflow.

#### 4. EXECUTIVE ROI (Cost Avoidance)
- **[FR]** Suppression de ~100 km de câbles erronés du budget initial (Cost Avoidance). Temps de production du livrable client divisé par 100.
- **[EN]** Eradication of ~100 km of ghost cables from the CAPEX baseline (Cost Avoidance). Client deliverable production time slashed by 99%.

#### 5. TECH STACK & EXECUTION
**Stack :** QGIS, Python 3.12 (PyQGIS), Pandas, Git.

### 🏗️ CORE-1 : Advanced Spatial Logic Routing (Tramway T8)
- **[Delivered: 2026-10-28]**

#### 1. ENTERPRISE MISSION & SCENARIO
- **[FR]** Pilotage automatisé des dévoiements réseaux (OSP) sur un projet d'infrastructure lourde (Tram T8), avec routage conditionnel Backbone vs DRET.
- **[EN]** Automated OSP utility relocation management for Heavy Civils, featuring conditional spatial routing for Backbone vs DRET.

#### 2. THE BOTTLENECK
- **[FR]** DXF sources corrompus (Dangling Nodes) bloquant l'extraction spatiale et générant des surcoûts matériels (GIGO).
- **[EN]** Corrupted source DXF files (Dangling Nodes) blocking spatial extraction and generating material overcosts (GIGO).

#### 3. THE AUTOMATED SOLUTION
- **[FR]** Pipeline Python de "Topology Healing" (Snapping/Dissolve) suivi d'un moteur de routage croisant l'intersection chirurgicale et l'extraction binaire.
- **[EN]** Python "Topology Healing" pipeline (Snapping/Dissolve) followed by a routing engine blending surgical intersection and binary extraction.

#### 4. EXECUTIVE ROI (Cost Avoidance)
- **[FR]** Zero-Touch Data Flow : 100% des erreurs CAO contournées automatiquement, visibilité CAPEX/OPEX immédiate via Dashboard.
- **[EN]** Zero-Touch Data Flow: 100% of CAD errors bypassed automatically, immediate CAPEX/OPEX visibility via Dashboard.

#### 5. TECH STACK & EXECUTION
**Stack :** Python 3.12, PyQGIS, QGIS Processing (Snap, Dissolve, Intersection, ExtractByLocation)

### 🏗️ LAB_CORE1_S02 : PostGIS Spatial Data Normalization
- **[Delivered: 2026-11-03]**

#### 1. ENTERPRISE MISSION & SCENARIO
- **[FR]** Standardiser les flux de données spatio-financiers pour les infrastructures OSP lourdes via une source de vérité relationnelle.
- **[EN]** Standardize spatio-financial data flows for heavy OSP infrastructure via a relational source of truth.

#### 2. THE BOTTLENECK
- **[FR]** L'ingestion sans contrainte provoque du GIGO, des doublons de projets, et des erreurs de rapports CAPEX.
- **[EN]** Unconstrained ingestion causes GIGO, project duplication, and CAPEX reporting errors.

#### 3. THE AUTOMATED SOLUTION
- **[FR]** BDD SQLite avec `PRIMARY KEY` stricte sur l'ID projet, interfacée avec Pandas pour une agrégation analytique rapide.
- **[EN]** SQLite DB with strict `PRIMARY KEY` on project ID, bridged with Pandas for rapid analytical aggregation.

#### 4. EXECUTIVE ROI (Cost Avoidance)
- **[FR]** Bloque 100% des doublons à l'ingestion ; agrégation des coûts instantanée sans consolidation manuelle.
- **[EN]** Blocks 100% of duplicates at ingestion; instant cost aggregation without manual consolidation.

#### 5. TECH STACK & EXECUTION
**Stack :** Python 3.12, SQLite3, Pandas
```bash
# Architecture Validation & Code Integration
git add osp_db_schema.py osp_db_insert.py osp_db_pandas.py
git add TECH_GLOSSARY_MASTER.md README.md index.md
git commit -m "feat(core1): deploy strict relational schema and Pandas ETL pipeline"
git push origin main