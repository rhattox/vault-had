import os

def find_secrets_yaml(directory):
    for root, dirs, files in os.walk(directory):
        if 'secret.yaml' in files:
            print(f"Found secrets.yaml file in: {root}")
            # TODO
            # Execute read_secret.py function

root_directory = './secrets/'

find_secrets_yaml(root_directory)

