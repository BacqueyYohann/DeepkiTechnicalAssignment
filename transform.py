import os
import gzip
import shutil
import pandas as pd

RAW_DIR = 'data/raw'
CLEAN_DIR = 'data/clean'
os.makedirs(CLEAN_DIR, exist_ok=True)


def extract_gz_files():
    for filename in os.listdir(RAW_DIR):
        if filename.endswith('.csv.gz'):
            gz_filepath = os.path.join(RAW_DIR, filename)
            extracted_filepath = os.path.join(RAW_DIR, filename[:-3]) 

            with gzip.open(gz_filepath, 'rb') as f_in:
                with open(extracted_filepath, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)


def load_and_clean_data():
    for filename in os.listdir(RAW_DIR):
        if filename.endswith('.csv'):
            filepath = os.path.join(RAW_DIR, filename)

            df = pd.read_csv(filepath)

            # removing useless columns for the usecase
            df_clean = df.drop(columns=['area_in_meters', 'confidence', 'geometry'], errors='ignore')

            # saving the result as CSV in the clean directory
            clean_filepath = os.path.join(CLEAN_DIR, filename)
            df_clean.to_csv(clean_filepath, index=False)


def transform_data():

    extract_gz_files()

    load_and_clean_data()
    
    print("Data transformation complete.")
