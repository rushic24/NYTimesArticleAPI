import unittest
import os


class nytimesarticlev2Tests(unittest.TestCase):
    def __init__(self):
        self.api_key = os.environ["NYT_API_KEY"]
