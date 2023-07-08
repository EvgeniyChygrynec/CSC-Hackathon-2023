import torch
from transformers import DataCollatorForLanguageModeling, Trainer, TrainingArguments
from transformers import T5ForConditionalGeneration
from prepare_tokenizer import df, tokenizer


model = T5ForConditionalGeneration.from_pretrained('t5-base')
max_length = 128

class QADataset(torch.utils.data.Dataset):
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

        question_tokens = self.tokenizer.encode(question, add_special_tokens=True, truncation=True,
                                                max_length=self.max_length - 1)
        answer_tokens = self.tokenizer.encode(answer, add_special_tokens=True, truncation=True,
                                              max_length=self.max_length - len(question_tokens) - 1)

        input_ids = question_tokens + answer_tokens

        padding_length = self.max_length - len(input_ids)
        input_ids += [self.tokenizer.pad_token_id] * padding_length

        return torch.tensor(input_ids)


questions = df['question'].tolist()
answers = df['answer'].tolist()


dataset = QADataset(questions, answers, tokenizer, max_length)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False
)

training_args = TrainingArguments(
    output_dir='./model_output',
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=32,
    save_steps=1000,
    save_total_limit=2
)




trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset
)

trainer.train()

trainer.save_model('./trained_model')
