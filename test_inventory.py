from inventory_manager import Inventory

def test_display(capsys): #using capsys to access the output of display functions.
  inventory = Inventory("malt", 50, 500)
  inventory.display()
  
  captured = capsys.readouterr() #used for reading and checking the output.
  assert "Product: malt" in captured.out #assert if the ouput contains what i expected.
  

  