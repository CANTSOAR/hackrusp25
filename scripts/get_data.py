from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

#uri = "mongodb+srv://<db_username>:<db_password>@cluster0.nsr4b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
uri = "mongodb+srv://ryanchwang:aO0oL36ytNgOpNyH@apollo.nsr4b.mongodb.net/?retryWrites=true&w=majority&appName=Apollo"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)