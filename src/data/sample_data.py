import random
import os
from datasets import load_dataset
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def save_splits(splits, file_path):
    with open(file_path, 'w') as f:
        for split in splits:
            f.write(f"{split}\n")

def sample_data(dataset_name, dataset_type, split_ratio, seed, output_dir, lang_multi=None):

    logging.info(f"Processing dataset: {dataset_name} for language: {lang_multi}")
    
    random.seed(seed)
    
    os.makedirs(output_dir, exist_ok=True)
    
    dataset = load_dataset(dataset_name)
    
    if dataset_type == "aya":
        dataset = dataset.filter(lambda example: example['language'] == lang_multi)
        dataset = dataset.filter(lambda example: example['inputs'] != "" and example['targets'] != "")
    
    elif dataset_type == "alpaca":
        dataset = dataset.filter(lambda example: example['output'] is not None and example['output'] != "")
        dataset = dataset.filter(lambda example: example['instruction'] != "" and example['instruction'] is not None)
        dataset = dataset.filter(lambda example: example['input'] is not None)
        
    else:
        logging.error(f"Incorrect dataset type {dataset_type}! Only Aya and Alpaca Datasets are supported!")
        return
    train_test_split = dataset['train'].train_test_split(test_size=split_ratio, seed=seed)

    train_dataset = train_test_split['train']
    test_dataset = train_test_split['test']
    
            
        
    dataset_name = dataset_name.split("/")[1]
    if lang:
        lang_suffix = lang.lower()
        train_split_path = os.path.join(output_dir, f"{dataset_name}_{lang_suffix}_train_split.txt")
        test_split_path = os.path.join(output_dir, f"{dataset_name}_{lang_suffix}_test_split.txt")
    else:
        train_split_path = os.path.join(output_dir, f"{dataset_name}_train_split.txt")
        test_split_path = os.path.join(output_dir, f"{dataset_name}_test_split.txt")
    save_splits(train_dataset, train_split_path)
    save_splits(test_dataset, test_split_path)
    
    logging.info(f"Saved indices for dataset: {dataset_name} and language: {lang}")

def main():
    datasets = [("CohereForAI/aya_dataset", "aya"), 
                ("Saugatkafley/alpaca-nepali-sft", "alpaca"), 
                ("iamshnoo/alpaca-cleaned-hindi", "alpaca")
                ]
    languages = ["Hindi", "Nepali"]
    split_ratio = 0.2
    seed = 42
    output_dir = "data_splits"
    
    for dataset_name, dataset_type in datasets:
        if dataset_type == "aya":
            for lang in languages:
                sample_data(dataset_name, dataset_type, split_ratio, seed, output_dir, lang)
        else:
            sample_data(dataset_name, dataset_type, split_ratio, seed, output_dir)
    

if __name__ == "__main__":
    main()
