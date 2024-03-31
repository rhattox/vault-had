import os

secrets_files = ['secrets.yaml', 'secrets.yml', 'secret.yaml', 'secret.yml' ]

def find_secrets_yaml(directory):
    for root, dirs, files in os.walk(directory):
        for multiple_secrets in secrets_files:
            if multiple_secrets in files:
                print(f"Found file in: {root}")
                print(dirs)
                print(files)


