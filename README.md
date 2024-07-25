# csv_vault_generator
A demo tool to dynamically create a Vault - including schema and data - from a CSV. Runs in the shell.

This intends to show the power of the Skyflow API first approach and employs both the Control and Data API's

Before running the tool, you need to perform pre-setup tasks
You need to have a Skyflow Try environment account (login)

Login to your Skyflow Studio (assuminng you are a vault owener or administrator)

Create an Account level "**Service Account**"
The service account MUST have the following Assignments & Roles:
 - Assignment:  Account-Level     Role:  "Account Admin"
 - Assignment:  Workspace-level   Role:  "Vault Creator" and  "Workspace Admin"
 - SAVE the settings and generate a **credentials.json** file.  (You will be requested for this file when the script runs!)

In the "csv_vault_generator" repo, there is a file:   **skyflow_params.json**
Edit this file and change **ALL** the parameter values to the ones associated with your Skyflow Account and environment

All done!  You are ready to run the geenrator.
The generator should take any "Strcutured Data" CSV file you provide.  A few samples are provided in the distribution and have been used to validate correct operation.
If you want to generate your own test data, you can use any tool of you choice or an online utility like e.g. Mockaroo:  https://www.mockaroo.com/

Now run the generator:   csvFileLoad.py   and follow the prompts.
> python3 csvFileLoad.py 
 
