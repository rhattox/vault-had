import requests
import json

def check_vault_secret_engine(vault_address,vault_port,vault_root_token, data):
    # print(data)
    var_url = f"http://{vault_address}:{vault_port}/v1/{data['namespace']}"
    var_headers = {
        "X-Vault-Token": f"{vault_root_token}"
    }
    response = requests.get(var_url, headers=var_headers)
    if 'errors' in response.json():
        print(f"ns '{data['namespace']}' doesn't exists")
        print("You will need to create it manually, then run it again...")
        return False
    else:
        return True


def call_vault_api(vault_address,vault_port,vault_root_token,data):
    # print(data)   
    # print(data['namespace'])
    curl_obj = {}
    
    curl_obj['data'] = data['stringData']
    


    json_data = json.dumps(curl_obj)
    # print(json_data)
    # var_url = f"http://{vault_address}:{vault_port}/v1/kv/data/example"
    var_url = f"http://{vault_address}:{vault_port}/v1/{data['namespace']}/data/{data['name']}"
    var_headers = {
        "X-Vault-Token": f"{vault_root_token}",
        "Content-Type": "application/json",
        "accept": "application/json",
    }
    response = requests.post(var_url, headers=var_headers, data=json_data)
    # print(response.json())
    if response.status_code == 200:
        # data_dict = json.loads(response.text)
        # print(data_dict)
        print(f"Create/Update secret {data['namespace']}")
    else:
        print('Error:', response.status_code)

