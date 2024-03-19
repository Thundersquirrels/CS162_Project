import json
import random

# does not help with creating good examples to improve accuarcy

def load_jsonl(input_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f]

def save_jsonl(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        for entry in data:
            json.dump(entry, f)
            f.write('\n')

def select_examples(data, examples_per_label=2):
    supports_examples = [entry for entry in data if entry['label'] == 'SUPPORTS']
    refutes_examples = [entry for entry in data if entry['label'] == 'REFUTES']
    
    selected_supports = random.sample([{'claim': e['claim'], 'label': e['label']} for e in supports_examples], examples_per_label)
    selected_refutes = random.sample([{'claim': e['claim'], 'label': e['label']} for e in refutes_examples], examples_per_label)

    return selected_supports + selected_refutes

def add_examples_to_dataset(data, examples):
    for entry in data:
        entry['examples'] = [e for e in examples if e['claim'] != entry['claim']]
    return data


data = load_jsonl('src/train_claims.jsonl')

examples = select_examples(data)

data_with_examples = add_examples_to_dataset(data, examples)

save_jsonl(data_with_examples, 'src/train_claims_with_examples.jsonl')
