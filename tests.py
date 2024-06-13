"""
Runs tests using unittest.
Automatically linked to github CI by the hooks in the .github/ directory.
Add your test files with import statements. Unittest will do the rest.
"""
# pylint: disable=unused-import

import unittest
from website_utils.easy_word_cloud import test_word_cloud

if __name__ == "__main__":
    unittest.main()
