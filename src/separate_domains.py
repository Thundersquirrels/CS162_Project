import json

def load_jsonl(input_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f]

def save_jsonl(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        for entry in data:
            json.dump(entry, f)
            f.write('\n')

def separate_domains(train_claims, predictions, predictions_with_examples, predictions_with_evidence):
    # sbic_claims = []
    # sbic_predictions = []
    sbic_predictions_with_examples = []
    sbic_predictions_with_evidence = []
    # mgfn_claims = []
    # mgfn_predictions = []
    mgfn_predictions_with_examples = []
    mgfn_predictions_with_evidence = []
    # health_claims = []
    # health_predictions = []
    health_predictions_with_examples = []
    health_predictions_with_evidence = []
    # climate_claims = []
    # climate_predictions = []
    climate_predictions_with_examples = []
    climate_predictions_with_evidence = []
    # hsd_claims = []
    # hsd_predictions = []
    hsd_predictions_with_examples = []
    hsd_predictions_with_evidence = []
    # toxigen_claims = []
    # toxigen_predictions = []
    toxigen_predictions_with_examples = []
    toxigen_predictions_with_evidence = []
    for idx, entry in enumerate(train_claims):
        if entry['domain'] == 'sbic':
            # sbic_claims.append(entry)
            # sbic_predictions.append(predictions[idx])
            sbic_predictions_with_examples.append(predictions_with_examples[idx])
            sbic_predictions_with_evidence.append(predictions_with_evidence[idx])
        if entry['domain'] == 'mgfn':
            # mgfn_claims.append(entry)
            # mgfn_predictions.append(predictions[idx])
            mgfn_predictions_with_examples.append(predictions_with_examples[idx])
            mgfn_predictions_with_evidence.append(predictions_with_evidence[idx])
        if entry['domain'] == 'health':
            # health_claims.append(entry)
            # health_predictions.append(predictions[idx])
            health_predictions_with_examples.append(predictions_with_examples[idx])
            health_predictions_with_evidence.append(predictions_with_evidence[idx])
        if entry['domain'] == 'climate':
            # climate_claims.append(entry)
            # climate_predictions.append(predictions[idx])
            climate_predictions_with_examples.append(predictions_with_examples[idx])
            climate_predictions_with_evidence.append(predictions_with_evidence[idx])
        if entry['domain'] == 'hsd':
            # hsd_claims.append(entry)
            # hsd_predictions.append(predictions[idx])
            hsd_predictions_with_examples.append(predictions_with_examples[idx])
            hsd_predictions_with_evidence.append(predictions_with_evidence[idx])
        if entry['domain'] == 'toxigen':
            # toxigen_claims.append(entry)
            # toxigen_predictions.append(predictions[idx])
            toxigen_predictions_with_examples.append(predictions_with_examples[idx])
            toxigen_predictions_with_evidence.append(predictions_with_evidence[idx])
    
    # save_jsonl(sbic_claims, 'out/domains/sbic_claims.jsonl')
    # save_jsonl(sbic_predictions, 'out/domains/sbic_predictions.jsonl')
    save_jsonl(sbic_predictions_with_examples, 'out/domains/sbic_predictions_with_examples.jsonl')
    save_jsonl(sbic_predictions_with_evidence, 'out/domains/sbic_predictions_with_evidence.jsonl')
    # save_jsonl(mgfn_claims, 'out/domains/mgfn_claims.jsonl')
    # save_jsonl(mgfn_predictions, 'out/domains/mgfn_predictions.jsonl')
    save_jsonl(mgfn_predictions_with_examples, 'out/domains/mgfn_predictions_with_examples.jsonl')
    save_jsonl(mgfn_predictions_with_evidence, 'out/domains/mgfn_predictions_with_evidence.jsonl')
    # save_jsonl(health_claims, 'out/domains/health_claims.jsonl')
    # save_jsonl(health_predictions, 'out/domains/health_predictions.jsonl')
    save_jsonl(health_predictions_with_examples, 'out/domains/health_predictions_with_examples.jsonl')
    save_jsonl(health_predictions_with_evidence, 'out/domains/health_predictions_with_evidence.jsonl')
    # save_jsonl(climate_claims, 'out/domains/climate_claims.jsonl')
    # save_jsonl(climate_predictions, 'out/domains/climate_predictions.jsonl')
    save_jsonl(climate_predictions_with_examples, 'out/domains/climate_predictions_with_examples.jsonl')
    save_jsonl(climate_predictions_with_evidence, 'out/domains/climate_predictions_with_evidence.jsonl')
    # save_jsonl(hsd_claims, 'out/domains/hsd_claims.jsonl')
    # save_jsonl(hsd_predictions, 'out/domains/hsd_predictions.jsonl')
    save_jsonl(hsd_predictions_with_examples, 'out/domains/hsd_predictions_with_examples.jsonl')
    save_jsonl(hsd_predictions_with_evidence, 'out/domains/hsd_predictions_with_evidence.jsonl')
    # save_jsonl(toxigen_claims, 'out/domains/toxigen_claims.jsonl')
    # save_jsonl(toxigen_predictions, 'out/domains/toxigen_predictions.jsonl')
    save_jsonl(toxigen_predictions_with_examples, 'out/domains/toxigen_predictions_with_examples.jsonl')
    save_jsonl(toxigen_predictions_with_evidence, 'out/domains/toxigen_predictions_with_evidence.jsonl')


train_claims = load_jsonl('src/train_claims.jsonl')
predictions = load_jsonl('out/train_claims_predictions.jsonl')
predictions_with_examples = load_jsonl('out/predictions_with_examples.jsonl')
predictions_with_evidence = load_jsonl('out/predictions_with_evidence.jsonl')

separate_domains(train_claims, predictions, predictions_with_examples, predictions_with_evidence)