import os
basedir=os.path.abspath(os.path.dirname(__file__))

SQL_ALCHEMY_DATABASE_URI='sqlite///'+os.path.join(basedir,'converter.db')
SQL_ALCHEMY_MIGRATED_REPO=os.path.join(basedir,'db_repository')
