from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
import logging

load_dotenv()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


MONGO_URI = os.getenv("MONGO_URI")


if not MONGO_URI:
    logger.error("MONGO_URI is not set in the environment variables.")
    raise EnvironmentError("MONGO_URI is not defined in the environment variables.")


try:
    client = AsyncIOMotorClient(MONGO_URI)
    database = client.get_database()
    students_collection = database.students
    logger.info("Successfully connected to MongoDB")
except Exception as e:
    logger.error(f"Error connecting to MongoDB: {str(e)}")
    raise ConnectionError(f"Failed to connect to MongoDB: {str(e)}")
