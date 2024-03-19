import json

with open('./generated-evidence.jsonl', 'r') as json_file:
    json_list = list(json_file)

with open('./generated-evidence-cleaned.jsonl', 'w') as clean_file:
    for json_str in json_list:
        result = json.loads(json_str)
        
        cleaned_string = result['final_response'].split('#')
        cleaned_string = ' '.join(cleaned_string[1:]) if len(cleaned_string) > 1 else cleaned_string[0]
        
        del result['label']
        del result['final_response']
        result['evidence'] = cleaned_string
        
        print(result)
        clean_file.write(json.dumps(result)+'\n')