import yaml

def source_secret_file(file_path):

    with open(file_path, 'r') as file:
        yaml_data = yaml.safe_load(file)
    
    vault_obj = {}
    
    name = yaml_data['metadata']['name']
    if name is None:
        print("metadata.name isn't set (yaml file)")
        exit(1)
    vault_obj['name'] = name
    
    #
    # TODO
    # 
    # Assume namespace default if it's empty

    namespace = yaml_data['metadata']['namespace']
    if namespace is None:
        print("metadata.namespace isn't set (yaml file)")
        print("assuming 'default' metadata.namespace")
        vault_obj['namespace'] = "default"
    vault_obj['namespace'] = namespace
    
    if yaml_data['data'] is None:
        print("data has no atribute, there is nothing to add")
        exit(1)
    else:
        data = {}
        for lenght in yaml_data['data'].items():
            data[f'{lenght[0]}'] = lenght[1]
    
    vault_obj['data'] = data
    
    # print(vault_obj)
    return(vault_obj)
