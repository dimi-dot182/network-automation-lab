Network Automation Lab (OSP Focus)

📌 Project Overview

This repository is a professional-grade sandbox dedicated to Network Automation with a specific focus on Outside Plant (OSP) operations. The goal is to bridge the gap between physical fiber infrastructure and software-defined networking.

Current features include:

Payload Validation: Robust JSON parsing for network inventories.

Resilience Logic: Advanced exception handling (try/except) for unstable API responses.

Data Integrity: Automated checks for missing keys in equipment databases.

🚀 Technical Stack

Language: Python 3.12+

Version Control: Git & GitHub

Environment: VS Code (English Interface)

🛠️ Installation & Setup

To clone this lab and run the scripts locally:

# Clone the repository
git clone https://github.com/dimi-dot182/network-automation-lab.git

# Enter the directory
cd network-automation-lab

# Run the data integrity script
python inventory_validator.py


🏗️ OSP Context

In the fiber industry, data integrity is critical. A single missing field in a GIS (Geographic Information System) export can lead to field intervention failures. This lab focuses on creating scripts that ensure every fiber node, splitter, and OLT entry is technically valid before deployment.

Author: Dimitri - Aspiring Network Automation Architect
**Contact:** [linkedin.com/in/dimitri-duperron]