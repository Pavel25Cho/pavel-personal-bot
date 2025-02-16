import os
import src.env
import src.spotify

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

src.env.load(ROOT_DIR)
# src.spotify.setup()