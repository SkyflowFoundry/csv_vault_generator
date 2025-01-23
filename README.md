# csv_vault_generator

## Overview
`csv_vault_generator` is a Python-based tool designed to securely load structured data from CSV files into a Skyflow Vault. This script facilitates seamless data ingestion while ensuring compliance with Skyflow's security standards.

## Prerequisites
Before running the script, ensure that you have the necessary dependencies installed.

### Python Installation
Ensure Python is installed on your system. You can check by running:
```sh
python --version
```
or
```sh
python3 --version
```

### Required Python Libraries
Install the required libraries using `pip` or `pip3`:
```sh
pip install requests pandas PyJWT
```

## Setup Instructions

### Skyflow Configuration
1. **Log in to Skyflow Studio** (Vault Owner or Administrator access required).
2. **Create an Account-Level "Service Account"**
   - The service account must have the following assignments and roles:
     - **Assignment:** Account-Level → **Role:** `Account Admin`
     - **Assignment:** Workspace-Level → **Role:** `Vault Creator`, `Workspace Admin`
   - **Save the settings and generate** a `credentials.json` file. This file will be required when running the script.

### Configure `skyflow_params.json`
Inside the repository, locate the file **`skyflow_params.json`** and update all parameter values to match your Skyflow Account and environment.

## Running the Generator
The generator is designed to process any structured CSV data file. Sample CSV files are provided in the repository to validate correct operation. You can also generate test data using tools like [Mockaroo](https://www.mockaroo.com/).

### Execute the Script
Run the generator script and follow the prompts:
```sh
python3 csvFileLoad.py
```

## Support
For any issues, please create a GitHub issue in this repository or refer to the Skyflow documentation for further assistance.
