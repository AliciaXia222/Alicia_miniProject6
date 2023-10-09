"""
Extract a dataset from a URL like Kaggle or data.gov. 
JSON or CSV formats tend to work well
"""
import os
import requests


def extract(
    url="""
    https://github.com/fivethirtyeight/data/blob/master/mad-men/performer-scores.csv?raw=true
    """,
    url2="""
    https://github.com/fivethirtyeight/data/blob/master/mad-men/show-data.csv?raw=true
    """,
    file_path="data/performer_scores.csv",
    file_path2="data/show_data.csv",
    directory="data",
):
    """Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    with requests.get(url2) as r:
        with open(file_path2, "wb") as f:
            f.write(r.content)
    return file_path, file_path2


