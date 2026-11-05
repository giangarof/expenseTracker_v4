import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load the .env file
load_dotenv()

# MongoDB connection URL
MONGODB_URL = os.getenv("DB_URL")

if not MONGODB_URL:
    raise RuntimeError("DB_URL is not set")

# Create the MongoDB client
client = MongoClient(MONGODB_URL, tls=True)

# Select the database
db = client["expense_tracker"]

# Select the collection
expenses_collection = db["expenses"]
income_collection = db["incomes"]

try:
    client.admin.command("ping")
    print("✅ MongoDB connected successfully!")
except Exception as e:
    print("❌ MongoDB connection failed:", e)
