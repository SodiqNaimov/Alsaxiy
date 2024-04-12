import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
full_path = BASE_DIR.joinpath('files', 'DataBase.db')
full_path_str = str(full_path)

# Replace backslashes with forward slashes
full_path_str = full_path_str.replace("\\", "/")

# Append a forward slash after '/cdn/media'
# full_path_str += '/'
db_path = full_path_str

# TOKEN
token = '5828429572:AAF-v2yuP5N3X9o6TnoJCWS6hJmT0Q2nZSg'
