import requests
import json


def get_dem_link(link, headers, cookies):
    response = requests.get(link, headers=headers, cookies=cookies)
    
    #res_text = response.text
    #state = json.loads(res_text, strict=False)
    #print(response.text)

    state = response.json()
    result = state['response']
    result = result[0]

    #json_filename = "json_file/" + result ['name']+".json"
    #print(json_filename)
    
    content = result['contents']

    dem = content[0]

    dem_link = result['name']+"/" + dem['name']
    """
    with open(json_filename, 'w', encoding='utf-8') as json_file:
        json.dump(state, json_file, ensure_ascii=False)
        print(json_filename + ":  write json file success!")
    """
    return dem_link
