# TODO - import relevant model and tokenizer modules from transformers
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# helper function provided to get model info
def get_model_info(model):
    ## model parameter type
    first_param = next(model.parameters())
    print(f"Model parameter dtype: {first_param.dtype}")

    ## which device the model is on
    device_idx = next(model.parameters()).get_device()
    device = torch.cuda.get_device_name(device_idx) if device_idx != -1 else "CPU"
    print(f"Model is currently on device: {device}")

    ## what is the memory footprint 
    print(model.get_memory_footprint())


def model_and_tokenizer_setup(model_id_or_path):
    
    model, tokenizer = None, None

    ##################################################
    # TODO: Please finish the model_and_tokenizer_setup.
    # You need to load the model and tokenizer, which will
    # be later used for inference. To have an optimized
    # version of the model, load it in float16 with flash 
    # attention 2. You also need to load the tokenizer, with
    # left padding, and pad_token should be set to eos_token.
    # Please set the argument trust_remote_code set to True
    # for both model and tokenizer load operation, as 
    # transformer verison is 4.36.2 < 4.37.0
    
    # End of TODO.
    ##################################################
    
    # Adapted from sample code: https://huggingface.co/microsoft/phi-2
    model = AutoModelForCausalLM.from_pretrained(model_id_or_path, torch_dtype=torch.float16, trust_remote_code=True)
    # attn_implementation="flash_attention_2"
    tokenizer = AutoTokenizer.from_pretrained(model_id_or_path, padding="max_length", padding_side="left", pad_token='<|endoftext|>', max_length=512, trust_remote_code=True)

    print(get_model_info(model))

    return model, tokenizer