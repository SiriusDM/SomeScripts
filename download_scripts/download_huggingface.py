from transformers import AutoModelForSeq2SeqLM
from transformers import AutoTokenizer
import datasets

prefix = 'file path prefix'
model_name = 'model name'

def download_dataset():
    dataset_name = 'dataset name'
    file_path = prefix + dataset_name
    dataset = datasets.load_dataset("dataset name")
    dataset.save_to_disk(file_path)

def download_model():
    file_path = prefix + model_name
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    model.save_pretrained(file_path)

def download_tokenizer():
    file_path = prefix + model_name + '-tokenizer'
    tokenizer = AutoTokenizer.from_pretrained('t5-small')
    tokenizer.save_pretrained(file_path)

if __name__ == "__main__":
    # download_dataset()
    # download_model()
    download_tokenizer()
