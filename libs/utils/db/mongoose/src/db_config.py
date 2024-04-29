from os import environ, path

from dotenv import dotenv_values

env_path = '.env'

if not path.exists(env_path):
    raise Exception('.env request_file not found')

config = dotenv_values(env_path)

DATABASE_URL = environ.get('DATABASE_URI')
DATABASE_NAME = config.get('DATABASE_NAME', 'api-pants-monorepo-db')
