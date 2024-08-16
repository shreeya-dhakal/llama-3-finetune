import pandas as pd
import re
import sys
sys.path.append("/Users/shreeyadhakal/Desktop/Projects-2023/llama-3-finetune/")

file_path = 'infer_out/alpaca_hindi_test_0809_50.csv'
df = pd.read_csv(file_path)

def extract_clean_response(text):
    match = re.search(r'### Response:(.*)', text, re.DOTALL)
    if match:
        response = match.group(1).strip()
        response = re.split(r'###', response)[0].strip()
        return response
    return None

df['cleaned_response'] = df['generated_text'].apply(extract_clean_response)

df[['generated_text', 'cleaned_response']].head()

output_file_path = 'infer_out/alpaca_cleaned_responses_hindi.csv'
df.to_csv(output_file_path, index=False)

output_file_path