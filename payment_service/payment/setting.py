from starlette.config import Config
from starlette.datastructures import Secret

try:
    # config = Config("e:/combine_project/Project-mart/payment_service/.env")
    config = Config(".env")  # Load environment variables from .env file

except FileNotFoundError:
    print("No .env file found, using default environment variables")
    config = Config()

DATABASE_URL = config.get("DATABASE_URL", cast=Secret)
TEST_DATABASE_URL = config.get("TEST_DATABASE_URL", cast=Secret)
BOOTSTRAP_SERVER = config.get("BOOTSTRAP_SERVER", cast=str)
KAFKA_PAYMENT_TOPIC = config.get("KAFKA_PAYMENT_TOPIC", cast=str)
KAFKA_CONSUMER_GROUP_ID_FOR_PAYMENT = config.get(
    "KAFKA_CONSUMER_GROUP_ID_FOR_PAYMENT", cast=str)
SCHEMA_REGISTRY_URL = config.get("SCHEMA_REGISTRY_URL", cast=str)
