from transformers import T5Tokenizer
import pandas as pd

import warnings
warnings.filterwarnings("ignore")


df = pd.read_csv('knowledge_base.csv')

df['question'] = df['question'].str.lower()
df['answer'] = df['answer'].str.lower()


tokenizer = T5Tokenizer.from_pretrained('t5-base')


df['question_tokens'] = df['question'].apply(lambda x: tokenizer.encode(x[:100], add_special_tokens=True))
df['answer_tokens'] = df['answer'].apply(lambda x: tokenizer.encode(x[:400], add_special_tokens=True))
