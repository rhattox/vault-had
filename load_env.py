from dotenv import load_dotenv
import requests
import os
import json
load_dotenv()

vault_port = os.getenv("VAULT_PORT")

if vault_port is None:
    print("vault_port isn't set")
    exit(1)

vault_address = os.getenv("VAULT_ADDRESS")

if vault_address is None:
    print("vault_address isn't set")
    exit(1)

vault_root_token = os.getenv("VAULT_ROOT_TOKEN")

if vault_root_token is None:
    print("vault_root_token isn't set")
    exit(1)


print(vault_port)
print(vault_address)
print(vault_root_token)

# Make a POST request with JSON data
response = requests.get(f"http://{vault_address}:{vault_port}/v1/kv/data/example", headers={"X-Vault-Token": f"{vault_root_token}"})

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content
    data_dict = json.loads(response.text)
    print(data_dict['data']['data'])
else:
    # Print an error message if the request was not successful
    print('Error:', response.status_code)
