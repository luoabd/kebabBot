"""This test file contains tests for various apis"""
import unittest

from tests import apis

class TestAPIs(unittest.TestCase):
    def test_get_trivia_response(self):
        self.assertEqual(apis.get_trivia_response(), 0)

    def test_get_wolframalpha_response(self):
        self.assertEqual(apis.get_wolframalpha_response(), "2")

    def test_get_translate_response(self):
        self.assertEqual(apis.get_translate_response(), 'Hello.')

    def test_get_reddit_response(self):
        self.assertIsInstance(apis.get_reddit_response(), str)

    def test_get_discord_response(self):
        self.assertEqual(apis.get_discord_response(), True)


if __name__ == '__main__':
    unittest.main()