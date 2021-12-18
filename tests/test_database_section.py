import os
import unittest

from configula import Configula


class TestDatabaseSectionConfigula(unittest.TestCase):
    """
    Performs test in section [database] of toml file
    """

    def test_with_mysql_1(self):
        toml_file = os.path.join(
            os.path.dirname(__file__), "examples", "papermerge_with_mysql_1.toml"
        )
        configula = Configula(
            config_locations=[toml_file],
            prefix='PAPERMERGE'
        )
        databases = configula.get_django_databases(proj_root='does_not_matter')
        self.assertEqual(
            databases['default']['ENGINE'],
            'django.db.backends.mysql'
        )

        self.assertEqual(
            databases['default']['ENGINE'],
            'django.db.backends.mysql'
        )
        self.assertEqual(
            databases['default']['USER'],
            'user1'
        )

        self.assertEqual(
            databases['default']['PORT'],
            3306
        )

    def test_with_postgres_1(self):
        toml_file = os.path.join(
            os.path.dirname(__file__), "examples", "papermerge_with_postgres_1.toml"
        )
        configula = Configula(
            config_locations=[toml_file],
            prefix='PAPERMERGE'
        )
        databases = configula.get_django_databases(proj_root='does_not_matter')

        self.assertEqual(
            databases['default']['ENGINE'],
            'django.db.backends.postgresql_psycopg2'
        )

        self.assertEqual(
            databases['default']['USER'],
            'user1'
        )

        self.assertEqual(
            databases['default']['PORT'],
            5432
        )

    def test_with_sqlite3(self):
        toml_file = os.path.join(
            os.path.dirname(__file__), "examples", "papermerge_with_sqlite.toml"
        )
        configula = Configula(
            config_locations=[toml_file],
            prefix='PAPERMERGE'
        )
        databases = configula.get_django_databases(proj_root='/home/here/')

        self.assertEqual(
            databases['default']['ENGINE'],
            'django.db.backends.sqlite3'
        )

        self.assertEqual(
            databases['default']['NAME'],
            '/home/here/db.sqlite3'
        )

