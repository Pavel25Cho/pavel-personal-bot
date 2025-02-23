import os, logging, sys

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

import src.env as env

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
env.load(ROOT_DIR)

import src.spotify as spotify
# import src.telegram as telegram

spotify.setup()