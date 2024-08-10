import os
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

def automated_crypto_pull():
    url = r'https://coinmarketcap.com/currencies/bitcoin/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Extracting the cryptocurrency name and price
    span_element = soup.find('span', class_="sc-65e7f566-0 lsTl")
    crypto_name = span_element.contents[0]
    crypto_price = soup.find('span', class_="sc-65e7f566-0 clvjgF base-text").text
    final_price = crypto_price.replace('$', '')

    # Getting the current timestamp
    dt = datetime.now()

    # Creating a dictionary with the data
    data = {
        'CryptoName': crypto_name,
        'Crypto Price': final_price,
        'TimeStamp': dt
    }

    # Creating a DataFrame from the dictionary
    df = pd.DataFrame([data])

    # Define the file path
    file_path = r'D:\MASTERS\pyth\Projects\Project 5\Bitcoinwebpuller.csv'

    # Check if the file exists
    if not os.path.exists(file_path):
        # If the file does not exist, create it and write the header
        df.to_csv(file_path, mode='w', header=True, index=False)
    else:
        # If the file exists, append the new data without writing the header
        df.to_csv(file_path, mode='a', header=False, index=False)

    print(df)

# Running the script every 10 seconds
while True:
    automated_crypto_pull()
    time.sleep(1)
