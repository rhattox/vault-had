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

