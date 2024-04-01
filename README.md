# vault-had
Vault Http Automated Deployer

This is a simple project to automate vault secret creation, this is intended to migrate all secrets from local files (secrets.yaml) to vault files

# How to use it:

Create an enviroment variable file in the root directory
```
VAULT_PORT=
VAULT_ADDRESS=
VAULT_ROOT_TOKEN=
SECRETS_DIR=
DEFAULT_NAMESPACE=
```

`SECRETS_DIR` should have the absolute path to avoid any problems.

# Secrets

It has to have `namespace` metadata. If it doesn't it will assume the variable `DEFAULT_NAMESPACE`.


`metadata.name` --> Will be used as the secret name under a kv store, which means...


`metadata.namespace` --> will be the KV secret path


secrets --> metadata.namespace --> metadata.name


# Secrets as Files

Not available yet
