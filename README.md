# Overview
We will fine-tune LLaMA 3 for Nepali and Hindi. Both Nepali and Hindi belong to the Indo-Aryan Family of languages and use Devanagari scripts. In addition, Nepali and Hindi have overlapping vocabularies. In contrast to Nepali which is a low-resource language, Hindi is considered high resource. 

# Purpose of the work
The purpose of this study is to understand:
- How LLaMA performs for each of these languages?
- The assumption is that the perfomance on Hindi is better, as it is a high resource language and is among the list of languages that meta.ai, which runs on LLaMA 3 lists as one of the languages it can communicate in, while Nepali is not listed.
- Understand cross-lingual ability of LLaMA-3
- Can we imporve the performance on Nepali for LLaMA 3 8B with LoRA?

# Datasets
We will be randomly splitting Alpaca and Aya datasets into test and train. We will use Aya for evaluation only, which Alpaca dataset will be use for both training and evaluation.
- Evaluation Data:
    - Test Split from [Alpaca Cleaned](https://huggingface.co/datasets/yahma/alpaca-cleaned)
    - Test Split from [Aya Dataset](https://huggingface.co/datasets/CohereForAI/aya_dataset)

- Fine-tuning Data:
    - Train Split from [Alpaca Cleaned](https://huggingface.co/datasets/yahma/alpaca-cleaned)

# Platform
- [Unsloth](https://github.com/unslothai/unsloth) packakge for fine-tuning
- Kaggle for running finetuning

