"""
Extract a dataset from a URL

central park dataset
"""
import os
import requests

def extract(
    url="""
    https://raw.githubusercontent.com/mattharrison/datasets/master/data/central-park-raw.csv
    """, 
    file_path="data/central-park-raw.csv",
    directory = "data"
):
    """"Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path



