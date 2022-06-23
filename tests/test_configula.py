import os
import pytest
import unittest

from configula import Configula


class TestConfigula(unittest.TestCase):

    def setUp(self):
        self.toml_file = os.path.join(
            os.path.dirname(__file__), "examples", "papermerge.toml"
        )
        self.configula = Configula(
            config_locations=[self.toml_file]
        )

    def test_instanciate_without_params(self):

        config = Configula()

        assert config.prefix == 'PAPERMERGE'  # default prefix
        assert config.delimiter == '__'  # default delimiter
        assert config.config_env_var_name == 'PAPERMERGE__CONFIG'

    def test_boolean_values(self):
        self.toml_file = os.path.join(
            os.path.dirname(__file__), "examples", "papermerge_boolean.toml"
        )
        config = Configula(config_locations=[self.toml_file])

        # the ``true`` value of the variable when present in toml file
        # is returned indeed as python ``True``
        assert config.get('main', 'positive_value') is True
        # the ``false`` values of variable when present in toml file
        # is returned as python ``False``
        assert config.get('main', 'negative_value') is False

        # non existing value resolves to default value provided
        # as 3rd argument
        assert config.get('main', 'non_existing_value', default=False) is False
        # Given the fact that default value is NOT provided - non
        # existing values will resolve to ``None``
        assert config.get('main', 'non_existing_value') is None

    def test_basic_positive_get(self):
        """Retrieves an existing value from confuration file"""
        value = self.configula.get('ocr', 'default_language')

        assert value == 'deu'

    def test_basic_negative_get(self):
        """
        If configuration does not exist - neither in configuration
         file nor as environment variable - returns None.
        """

        value = self.configula.get('ocr', 'non_existing_blah')
        assert value is None

    def test_environ_vars_override_toml(self):
        """Env variables will override toml configurations"""
        value_before_test = os.getenv('PAPERMERGE__OCR__DEFAULT_LANGUAGE')

        # this env variable will override configuration file's value:
        #  [ocr]
        #  default_language='deu'
        os.environ['PAPERMERGE__OCR__DEFAULT_LANGUAGE'] = 'ron'

        value = self.configula.get('ocr', 'default_language')
        assert value == 'ron'

        # clean up test
        if value_before_test:
            os.environ['PAPERMERGE__OCR__DEFAULT_LANGUAGE'] = value_before_test
