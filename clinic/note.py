from datetime import date

class Note:
  def __init__(self, code: int, text: str): 
    self.__code = code
    self.__text = text
    
    # getting today's time
    today = date.today()
    
    # formating today's date 
    date_written = today.strftime('%B %d, %Y')
    
    # setting Note's date_written field to date_written
    self.__date_written = date_written
  
  def __eq__ (self, other):
    if other == None:
      return False
    
    else:
      
      # NOTE: when timestamp is implemmented, include a timestamp comparison
      # Ex. self.__timestamp == other.__timestamp
      return self.__code == other.__code and self.__text == other.__text and self.__date_written == other.__date_written
    
  def get_text(self):
    return self.__text
  
  def update_text(self, new_text: str):
    # NOTE: if note is updated, the self.__date_written will be updated to the time it was updated
    
    # getting today's time
    today = date.today()
    
    # formating today's date 
    date_written = today.strftime('%B %d, %Y')
    
    # setting Note's date_written field to the updated date_written
    self.__date_written = date_written 
    
    self.__text = new_text