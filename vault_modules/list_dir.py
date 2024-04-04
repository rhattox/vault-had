import os

secrets_files = ['secrets.yaml', 'secrets.yml', 'secret.yaml', 'secret.yml' ]

files_array = []

def find_secrets_yaml(directory):
    for root, dirs, files in os.walk(directory):
        for multiple_secrets in secrets_files:
            if multiple_secrets in files:
                file_path = f"{root}/{multiple_secrets}"
                files_array.append(file_path)
                print(f"Adding {file_path}")

    if len(files_array) == 0:
        print("No secret file was found!")
        print(f"Check your SECRET_DIR={ directory } on the .env file contains any: ")
        print("secrets.yaml")
        print("secret.yaml")
        print("secrets.yml")
        print("secret.yml")
    return files_array

