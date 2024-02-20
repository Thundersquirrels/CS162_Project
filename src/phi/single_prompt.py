import torch

import argparse
from tqdm import tqdm
from phi.phi_utils.model_setup import model_and_tokenizer_setup

torch.set_default_device("cuda")

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_id_or_path', type=str, required=True)
    parser.add_argument('--single_prompt', type=str, required=True)
    parser.add_argument('--test_prompting', action="store_true", default=False)
    args = parser.parse_args()
    return args 

def single_prompt(model, tokenizer, prompt):    
    ##############################################################
    # TODO: Please complete the implementation of this 
    # fn. You need to tokenize a single prompt, generate outputs 
    # for it, and then decode the output back to regular text. 

    # End of TODO.
    #############################################################
    
    input_ids = tokenizer(prompt, return_tensors="pt")["input_ids"].to(torch.device("cuda"))
    attention_mask = (input_ids != tokenizer.pad_token_id).type(torch.float)

    with torch.no_grad():
        outputs = model.generate(input_ids, attention_mask=attention_mask, max_new_tokens=50)
    
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    print("Model Response: ", text)

def main(args):
    
    model, tokenizer = model_and_tokenizer_setup(args.model_id_or_path)
    single_prompt(model=model, tokenizer=tokenizer, prompt=args.single_prompt)


if __name__ == "__main__":
    args = parse_args()
    main(args)