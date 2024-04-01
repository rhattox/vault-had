import vault_modules.load_env as load_env
import vault_modules.list_dir as list_dir
import vault_modules.read_secret as read_secret
import vault_modules.vault_request as vault_request

vault_port, vault_address, vault_root_token, secrets_dir = load_env.load_environments_variables()

# print(vault_port)
# print(vault_address)
# print(vault_root_token)
# print(secrets_dir)

file_array = list_dir.find_secrets_yaml(secrets_dir)

# print(file_array)

for path in file_array:
    data = read_secret.source_secret_file(path)
    vault_request.call_vault_api(vault_address, vault_port, vault_root_token, data)
