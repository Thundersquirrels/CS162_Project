import pandas as pd
from torch.utils.data import Dataset
from utils.file_utils import load_jsonl
from phi.phi_utils.constants import PHI_ZERO_SHOT_EVAL_PROMPT, PHI_FEW_SHOT_EVAL_PROMPT, PHI_ZERO_SHOT_EVIDENCE_EVAL_PROMPT, PHI_ZERO_SHOT_EVIDENCE_PROMPT

class PhiPromptDataset(Dataset):
    def __init__(self, annotations_filepath, prompt_type, evidence_filepath = None):
        self.data = load_jsonl(annotations_filepath)
        self.prompt_type = prompt_type

        if evidence_filepath is not None: 
            self.evidence_data = load_jsonl(evidence_filepath)
        else:
            self.evidence_data = None

    def __len__(self):
        return len(self.data)

    ############################################################
    # TODO: Please complete the implementation for the
    # the following transform functions and __getitem__ fn, that you 
    # will use in def __getitem__ to convert a sample into prompt.
    # You can use the templates provided to in the constants.py file

    # End of TODO.
    ##################################################

    def zero_shot_eval_prompt_transform(self, claim, task_type):
        return PHI_ZERO_SHOT_EVAL_PROMPT.format(claim=claim, task_type=task_type)
    
    def few_shot_eval_prompt_transform(self, examples, claim, task_type):
        return PHI_FEW_SHOT_EVAL_PROMPT.format(examples=examples, claim=claim, task_type=task_type)
    
    def zero_shot_evidence_prompt_transform(self, information, claim):
        return PHI_ZERO_SHOT_EVIDENCE_PROMPT.format(information=information, claim=claim)
    
    def zero_shot_evidence_evaluate_prompt_transform(self, evidence, claim, task_type):
        return PHI_ZERO_SHOT_EVIDENCE_EVAL_PROMPT.format(evidence=evidence, claim=claim, task_type=task_type)
    
    def __getitem__(self, idx):
        ##################################################
        # TODO: Please complete the implementation of __getitem__
        # You may use if-else statements to choose the prompt
        # transform as per the prompt type given to you.
        
        # End of TODO.
        ##################################################
        
        claim = self.data[idx]['claim']
        
        if self.prompt_type == "zero_eval":
            task_type = self.data[idx]['task_type']
            return self.zero_shot_eval_prompt_transform(claim=claim, task_type=task_type)
        
        if self.prompt_type == "few_eval":
            task_type = self.data[idx]['task_type']
            examples = self.data[idx]['examples']
            return self.few_shot_eval_prompt_transform(examples=examples, claim=claim, task_type=task_type)
        
        if self.prompt_type == "zero_evidence":
            information = self.data[idx]['information']
            return self.zero_shot_evidence_prompt_transform(information=information, claim=claim)
        
        if self.prompt_type == "zero_evidence_eval":
            task_type = self.data[idx]['task_type']
            evidence = self.evidence_data[idx]['evidence_sample']
            return self.zero_shot_evidence_evaluate_prompt_transform(evidence=evidence, claim=claim, task_type=task_type)
            