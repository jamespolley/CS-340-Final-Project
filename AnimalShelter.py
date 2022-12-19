from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
  """ CRUD operations for Animal collection in MongoDB """

  def __init__(self, username, password):
    # Initializing the MongoClient. This helps to 
    # access the MongoDB databases and collections. 
    self.client = MongoClient('mongodb://%s:%s@localhost:54232/?authSource=AAC' % (username, password))
    self.database = self.client['AAC']

  def create(self, data):
    # Create a new record
    # 
    # confirm data to save is not empty
    if data is not None:
      # data should be dictionary, save status
      insertStatus = self.database.animals.insert_one(data)
      # returns true if successful, otherwise false
      return insertStatus.acknowledged
    raise Exception("Nothing to save. Parameter is empty")

  def read(self, data):
    # Read an existing record
    # 
    # If search data exists, return it
    if data:
      return self.database.animals.find(data, {"_id": False})
    # Otherwise, return all records
    return self.database.animals.find({}, {"_id": False})

  def update(self, query, data):
    # Update an existing record
    # 
    # Confirm data to save is not empty
    if data is not None:
      self.database.animals.update_many(query, {"$set":data})
      print("Updated")
    else:
      raise Exception("Can't update. Query is empty.")
      
  def delete(self, data):
    # Delete an existing record
    # 
    # Confirm data to save is not empty
    if data is not None:
      self.database.animals.delete_many(data)
      print("Deleted")
    else:
      raise Exception("Can't delete. Query is empty.")