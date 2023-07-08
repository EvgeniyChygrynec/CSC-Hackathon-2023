import torch
from torch.utils.data import Dataset
from prepare_tokenizer import df, tokenizer

class QADataset(Dataset):
    def __init__(self, questions, answers, tokenizer, max_length):
        self.questions = questions
        self.answers = answers
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.questions)

    def __getitem__(self, idx):
        question = self.questions[idx]
        answer = self.answers[idx]

        encoding = self.tokenizer.encode_plus(
            question,
            answer,
            add_special_tokens=True,
            max_length=self.max_length,
            truncation=True,
            padding="max_length"
        )

        input_ids = encoding["input_ids"]

        return torch.tensor(input_ids)


questions = df['question'].tolist()
answers = df['answer'].tolist()
max_length = 128

dataset = QADataset(questions, answers, tokenizer, max_length)
print(dataset[0])