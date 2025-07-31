import uuid
from datetime import datetime

class Inventory:
  def __init__(self, product_name, quantity, price):
    self.name = product_name
    self.quantity = quantity
    self.price = price
    self.SKU = uuid.uuid4()
    
  def display(self):
    print(f"Product: {self.name}, Quantity: {self.quantity}, Price {self.price}, Product_ID: {self.SKU}")

class Inventory_Manager:
  def __init__(self):
    self.inventory = []
    
  def add_inventory(self, product_name, quantity, price): 
    if not isinstance(product_name, str):
      print("must be a valid input")
      
    if quantity <= 0:
      print("must be a valid number")
      
    if price.float() <= 0:
      print("must be a valid number")
      
    inventory = Inventory(product_name, quantity, price)
    
    self.inventory.append(inventory)
  
  import uuid

  def filter_inventory(self):
    # Ask user for category to filter
    user_input = input("Enter name of inventory category: ").lower().strip()

    filtered = []

    # Loop through each inventory item
    for item in self.inventory:
        if item['Category'].lower() == user_input:
            filtered.append(item)

    if not filtered:
        print("No transaction found for that category.")
    else:
        print("\nFiltered Transactions by Category:")
        for t in filtered:
            print(f"{t['product_name']} - {t['quantity']} - {t['price']} - {uuid.uuid4()}")

    return filtered
 
  
  def view_stock(self):
    pass 
  
  def total_inventory(self):
    pass
  
  def sell_items(self):
    pass
  
  def restock_item(self):
    pass
  pass

class FileHandler:
  def __init__(self):
    pass
  
  def load_file(self):
    pass
  
  def save_file(self):
    pass

class CliController:
  def __init__(self):
    pass
  
  def menu(self):
    pass
  
  def choice(self):
    pass
  
  def run(self):
    pass

if __name__ == "__main__":
  inventory = Inventory("malt", 50, 5000)
  inventory.SKU
  print(f"Generate uuid {inventory.SKU}")
  