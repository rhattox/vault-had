import vault_modules.load_env as load_env
import vault_modules.list_dir as list_dir

vault_port, vault_address, vault_root_token, secrets_dir = load_env.load_environments_variables()

print(vault_port)
print(vault_address)
print(vault_root_token)
print(secrets_dir)

list_dir.find_secrets_yaml(secrets_dir)
