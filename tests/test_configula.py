import os
import unittest

from configula import Configula


class TestConfigula(unittest.TestCase):

    def setUp(self):
        self.toml_file = os.path.join(
            os.path.dirname(__file__), "examples", "papermerge.toml"
        )
        self.configula = Configula(
            config_locations=[self.toml_file],
            prefix='PAPERMERGE'
        )

    def test_basic_positive_get(self):
        """Retrieves an existing value from confuration file"""
        value = self.configula.get('ocr', 'default_language')
        self.assertEqual(value, 'deu')

    def test_basic_negative_get(self):
        """
        If configuration does not exist - neither in configuration
         file nor as environment variable - returns None.
        """

        value = self.configula.get('ocr', 'non_existing_blah')
        self.assertIsNone(value)

    def test_environ_vars_override_toml(self):
        """Env variables will override toml configurations"""
        value_before_test = os.getenv('PAPERMERGE_OCR_DEFAULT_LANGUAGE')

        # this env variable will override configuration file's value:
        #  [ocr]
        #  default_language='deu'
        os.environ['PAPERMERGE_OCR_DEFAULT_LANGUAGE'] = 'ron'

        value = self.configula.get('ocr', 'default_language')
        self.assertEqual(value, 'ron')

        # clean up test
        if value_before_test:
            os.environ['PAPERMERGE_OCR_DEFAULT_LANGUAGE'] = value_before_test

    def test_basic_positive_get_var(self):
        """Retrieves an existing value from confuration file"""
        value = self.configula.get_var('some_var')
        self.assertEqual(value, 100)

    def test_basic_negative_get_var(self):
        """
        If configuration does not exist - neither in configuration
         file nor as environment variable - returns None.
        """

        value = self.configula.get_var('non_existing_var')
        self.assertIsNone(value)
