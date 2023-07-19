from transformers import AutoModelForSeq2SeqLM
from transformers import AutoTokenizer
import datasets

prefix = ''
model_name = ''
access_token = ''

def download_dataset():
    dataset_name = 'imagenet-1k'
    file_path = prefix + dataset_name
    dataset = datasets.load_dataset(dataset_name, split=[''],use_auth_token=access_token, cache_dir='')
    dataset.save_to_disk(file_path)

def download_model():
    file_path = prefix + model_name
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    model.save_pretrained(file_path)

def download_tokenizer():
    file_path = prefix + model_name + '-tokenizer'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.save_pretrained(file_path)

if __name__ == "__main__":
    # download_dataset()
    # download_model()
    # download_tokenizer()
