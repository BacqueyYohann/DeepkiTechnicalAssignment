import os
import wget

# output path
OUTPUT_DIR = 'data/raw'
os.makedirs(OUTPUT_DIR, exist_ok=True)


def download_file(url: str):

    print(f"Downloading file from URL: {url}")
    filename = os.path.join(OUTPUT_DIR, os.path.basename(url))
    
    wget.download(url, filename)
    print(f"\nDownload completed. File saved at: {filename}")
    
    return filename

def download_csv_from_url(url: str):

    return download_file(url)
