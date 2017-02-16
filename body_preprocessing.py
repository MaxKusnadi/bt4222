
import pandas as pd
from bs4 import BeautifulSoup

ORIGINAL_DATASET = input("Enter the path of ur original csv path: ")
TARGET_DATASET = input("Enter the path of ur target csv path: ")

data = pd.read_csv(ORIGINAL_DATASET, encoding='latin1')


def get_string(text):
    soup = BeautifulSoup(text, 'html.parser')
    lst = []
    for p in soup.find_all('p'):
        lst.extend(list(map(lambda x: x.string if x.string else "", p.children)))
    return "".join(lst)


def is_code_present(text):
    soup = BeautifulSoup(text, 'html.parser')
    return 1 if soup.pre else 0

data['full_text'] = data['Body'].apply(get_string)
data['is_code_present'] = data['Body'].apply(is_code_present)
data.to_csv(TARGET_DATASET)
