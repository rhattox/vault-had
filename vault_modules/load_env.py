from dotenv import load_dotenv
import os


def load_environments_variables():

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
    
    secrets_dir = os.getenv("SECRETS_DIR")
    
    if secrets_dir is None:
        print("secrets_dir isn't set")
        exit(1)
    
    return vault_port, vault_address, vault_root_token, secrets_dir

