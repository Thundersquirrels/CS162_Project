import json

with open('./test_claims.jsonl', 'r') as json_file:
    json_list = list(json_file)

domains = set()

for json_str in json_list:
    result = json.loads(json_str)
    domains.add(result['domain'])
    
print(list(domains))