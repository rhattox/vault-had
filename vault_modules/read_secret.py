import yaml
import vault_modules.vault_request as vault_request

def source_secret_file(vault_address, vault_port, vault_root_token, file_path):

    with open(file_path, 'r') as file:
        yaml_data = yaml.safe_load(file)
    
    vault_obj = {}
    # Namespace = secret engine
    try: 
        namespace = yaml_data['metadata']['namespace']
        vault_obj['namespace'] = namespace
    except Exception as e:
        print("metadata.namespace isn't set (yaml file)")
        print("assuming 'default' metadata.namespace")
        vault_obj['namespace'] = "default"
    #
    # Todo
    #
    # Check if the secret engine exits 
    # Create a new if it doesn't
    
    # Name = secret name
    try:
        name = yaml_data['metadata']['name']
        vault_obj['name'] = name
    except Exception as e:
        print("metadata.name isn't set (yaml file)")
        exit(1)
    
    # print(yaml_data['data'])
    if yaml_data['stringData'] is None:
        print("data has no atribute, there is nothing to add")
        exit(1)
    else:
        data = {}
        for lenght in yaml_data['stringData'].items():
            data[f'{lenght[0]}'] = lenght[1]
    
    vault_obj['stringData'] = data
    
    vault_injection = vault_request.check_vault_secret_engine(vault_address, vault_port, vault_root_token, vault_obj)
    # print(vault_injection)

    if vault_injection == True:
        # print(vault_obj)
        return(vault_obj)
    else:
        return (False)
