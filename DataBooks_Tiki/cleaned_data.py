from bs4 import BeautifulSoup
import pandas as pd
import re
import requests
import os
from tqdm import tqdm  

# Đọc dữ liệu từ file crawled_data.csv
df = pd.read_csv('crawled_data.csv')

# Hàm để làm sạch dữ liệu
def clean_html_and_special_chars(text):
    # Xóa các thẻ HTML
    soup = BeautifulSoup(text, 'html.parser')
    text = soup.get_text()  
    # Xóa các ký tự đặc biệt
    text = re.sub(r'[^\w\s]', '', text) 
    return text

# Áp dụng hàm làm sạch cho cột 'description'
df['description'] = df['description'].apply(clean_html_and_special_chars)

# Loại bỏ các dòng có dữ liệu trống
df = df.dropna(subset=df.columns.difference(['price_usd']))

# Lưu DataFrame đã làm sạch vào file cleaned_data.csv
df.to_csv('cleaned_data.csv', index=False)