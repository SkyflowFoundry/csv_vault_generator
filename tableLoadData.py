import pandas as pd
import requests
import json
from datetime import datetime    # type: ignore 
from generateSchema import get_skyflow_params  # type: ignore

def batchLoad(directory, full_file, bearerToken, vault_id):
    batchCount = 0
    successful_records_count = 0  # Initialize the counter for successful records

    # Get Skyflow parameter details for run
    AccountId, Vault_URL, WorkspaceID, Vault_Name, Vault_Table_Name, Management_URL, user_id, Records_Batch_Size = get_skyflow_params(directory, bearerToken)

    # Initialize the records list
    records_list = []

    datetime1 = datetime.now()
    # Iterate csv rows in the DataFrame
    for index, row in full_file.iterrows():
        # Build fields dynamically using column headers
        fields = {column: str(row[column]) if isinstance(row[column], (int, float)) else row[column] for column in full_file.columns}

        # Record ....
        record = {
            "fields": fields
        }
        records_list.append(record)

    # Set the headers
    headers = {
        'Authorization': f'Bearer {bearerToken}',
        'Content-Type': 'application/json'
    }

    # Create the URL for the Batch API inserts
    url = f'{Vault_URL}/v1/vaults/{vault_id}/{Vault_Table_Name}'

    # Function to send a batch of records
    def send_batch(batch):
        records = {
            "records": batch,
            "tokenization": False
        }
        # print(json.dumps(records))  # debug: records to insert
        response = requests.post(url, headers=headers, data=json.dumps(records))
        return response

    all_successful = True

    # Process the records in batches
    for i in range(0, len(records_list), Records_Batch_Size):
        batchCount += 1
        batch = records_list[i:i + Records_Batch_Size]
        response = send_batch(batch)

        # Check the response
        if response.status_code == 200:
            print(f"Batch record set #{batchCount} created.")
            successful_records_count += len(batch)  # Increment the counter by the size of the current batch
        else:
            print(f"Failed to create batch records. Status code: {response.status_code}")
            print(response.text)
            all_successful = False

    # Output the total number of successfully processed records
    datetime2 = datetime.now()
    print(f"Total successfully processed records: {successful_records_count}")
    print(f"Load elapsed time: {elapsed_time(datetime1, datetime2)} seconds\n")

    return all_successful

def elapsed_time(datetime1, datetime2):
    elapsed_time = datetime2 - datetime1            #elapsed
    elapsed_seconds = elapsed_time.total_seconds()    #convert to total seconds
    return f"{elapsed_seconds:.2f}"    #elapsed - two decimal places
