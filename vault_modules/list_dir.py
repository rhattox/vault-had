import os

secrets_files = ['secrets.yaml', 'secrets.yml', 'secret.yaml', 'secret.yml' ]

files_array = []

def find_secrets_yaml(directory):
    for root, dirs, files in os.walk(directory):
        for multiple_secrets in secrets_files:
            if multiple_secrets in files:
                file_path = f"{root}/{multiple_secrets}"
                files_array.append(file_path)
                # print(f"Adding {file_path}")
    return files_array

