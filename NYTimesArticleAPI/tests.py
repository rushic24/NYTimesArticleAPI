import unittest
import os


class NYTimesArticleAPITests(unittest.TestSuite):
    def __init__(self):
        self.api_key = os.environ["NYT_API_KEY"]
