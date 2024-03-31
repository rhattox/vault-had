import yaml
# TODO
#
#   create a loop for every key inside data block 
#   and do a request puting this data to the namespace of the file
#   and using the name as example
#

yaml_file_path = 'secret.yaml'

with open(yaml_file_path, 'r') as file:
    yaml_data = yaml.safe_load(file)

vault_obj = {}



name = yaml_data['metadata']['name']
if name is None:
    print("metadata.name isn't set (yaml file)")
    exit(1)
vault_obj['name'] = name


namespace = yaml_data['metadata']['namespace']
if namespace is None:
    print("metadata.namespace isn't set (yaml file)")
    exit(1)
vault_obj['namespace'] = namespace


if yaml_data['data'] is None:
    print("data has no atribute, there is nothing to add")
    exit(1)
else:
    data = {}
    for lenght in yaml_data['data'].items():
        data[f'{lenght[0]}'] = lenght[1]


print(data)

vault_obj['data'] = data

print(vault_obj)
