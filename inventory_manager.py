import uuid
from datetime import datetime

class Inventory:
  def __init__(self, product_name, quantity, price):
    self.name = product_name
    self.quantity = quantity
    self.price = price
    self.SKU = uuid.uuid4()
    
    
  pass

class Inventory_Manager:
  pass

class FileHandler:
  pass

class CliController:
  pass

if __name__ == "__main__":
  inventory = Inventory("malt", 50, 5000)
  inventory.SKU
  print(f"Generate uuid {inventory.SKU}")
  