from os import path

from dotenv import dotenv_values

env_path = '.env'

if not path.exists(env_path):
    raise Exception('.env request_file not found')

config = dotenv_values(env_path)

DATABASE_URI = config.get('DATABASE_URI', 'mongodb://localhost:27017')
DATABASE_NAME = config.get('DATABASE_NAME', 'api-pants-monorepo-db')
