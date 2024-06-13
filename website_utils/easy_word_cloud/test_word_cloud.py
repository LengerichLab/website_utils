"""
Unit tests.
"""

import unittest

from website_utils.easy_word_cloud.word_cloud import (
    make_word_cloud_from_bibtex,
    make_word_cloud_from_text,
)


class TestWordCloud(unittest.TestCase):
    """
        Tester for the easy_word_cloud
    """
    def test_raw_text(self):
        """
        Test generation from raw text.
        :return: None
        """
        make_word_cloud_from_text(
            "Lorem ipsum dolor sit amet. Word cloud example maker. Word cloud example.",
            "website_utils/easy_word_cloud/test_output",
            "test_raw_cloud.png",
            show=False,
        )
        with open(
            "website_utils/easy_word_cloud/test_output/test_raw_cloud.png", "rb"
        ) as f:
            self.assertTrue(f.read())

    def test_example_bibtex(self):
        """
        Test generation from bibtex file.
        :return: None
        """
        make_word_cloud_from_bibtex(
            "website_utils/easy_word_cloud/example.bib",
            "website_utils/easy_word_cloud/test_output",
            "test_word_cloud.png",
            show=False,
        )
        # Check that the file was created
        with open(
            "website_utils/easy_word_cloud/test_output/test_word_cloud.png", "rb"
        ) as f:
            self.assertTrue(f.read())


if __name__ == "__main__":
    unittest.main()
