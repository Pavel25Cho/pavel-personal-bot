import os
from dotenv import load_dotenv

def load(root):
    dotenv_path = os.path.join(root, '.env')
    
    # Check if there is local environment variables file
    if os.path.exists(dotenv_path + '.local'):
        dotenv_path = dotenv_path + '.local'

    load_dotenv(dotenv_path)