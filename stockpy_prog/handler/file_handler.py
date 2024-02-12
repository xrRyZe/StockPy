import json
#disclaimer: this .py scrip was created heavily using GitHub-CoPilot and AI!


#---readers-------------------------------------------------------------
    #string
def read_json_file_as_string(path:str):
    with open(path, 'r') as f:
        data:str = f.read()
    return data

    #dict
        #whole file
def read_json_file_as_dict(path:str):
    with open(path, 'r') as f:
        data:dict = json.load(f)
    return data

        #specific key
def read_json_file_as_dict_wk(path:str, key:str): #wk = with key
    with open(path, 'r') as f:
        data:dict = json.load(f)
    return data[key]


#---writers-------------------------------------------------------------
    #string
def rewrite_json_file(path:str, data:str):
    with open(path, 'w') as f:
        f.write(data)

    #dict
def rewrite_json_file(path:str, data:dict):
    with open(path, 'w') as f:
        json.dump(data, f)


#---appenders-----------------------------------------------------------
    #string
def append_to_json_file(path:str, data:str):
    with open(path, 'a') as f:
        f.write(data)

    #dict
def append_to_json_file(path:str, data:dict):
    with open(path, 'a') as f:
        json.dump(data, f)


#---editors-------------------------------------------------------------
    #string
def edit_json_file(path:str, new_data:str, key:str):
    with open(path, 'r') as f:
        data:str = f.read()
    if key in data:
        data = data.replace(key, new_data)
    else:
        print('Key not found!')
        raise KeyError('Key not found!')
    
    with open(path, 'w') as f:
        f.write(data)

    #dict
def edit_json_file(path:str, new_data:dict, key:str):
    with open(path, 'r') as f:
        data:dict = json.load(f)
    if key in data:
        data[key] = new_data
    else:
        print('Key not found!')
        raise KeyError('Key not found!')
