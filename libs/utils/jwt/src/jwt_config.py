import uuid
from os import path

from dotenv import dotenv_values

env_path = '.env'

if not path.exists(env_path):
    raise Exception('.env file not found')

config = dotenv_values(env_path)

JWT_SECRET_KEY = config.get('JWT_SECRET_KEY', f'{uuid.uuid4()}')
ALGORITHM = config.get('ALGORITHM', 'HS256')

ACCESS_TOKEN_EXPIRE_IN_MINUTES = int(
    config.get('ACCESS_TOKEN_EXPIRE_IN_MINUTES', '10')
)
