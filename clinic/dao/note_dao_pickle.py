from .note_dao import * 
from ..note import *
from pickle import dump, load

from pathlib import Path
import os 

class NoteDAOPickle(NoteDAO):
  def __init__(self, patient_phn: int, autosave = False):
    self.autosave = autosave
    
    # the name of the file of the patient we want to access
    self.patient_phn = patient_phn
    
    # the file location where we will be saving the notes at
    self.filename = f'clinic/records/{self.patient_phn}.dat' 
    
    self.__patients_notes = {} 
    self.__autocounter = 0
    
    # if auto save is turned on, load notes there were saved
    # load_notes also changes self.__autocounter
    self.load_notes()
      
  def load_notes(self):
    # if auto save is turned on, load notes there were saved
    if self.autosave:
      try:
          with open(self.filename, 'rb') as file:
              self.__patients_notes = load(file)
      except:
        pass
          
      # count the number of note entries and set it as the autocounter
      self.__autocounter = len(list(self.__patients_notes.items()))    
  
  def search_note(self, key):
    # if there exist a note with the corresponding note_code, return note
    
    # Note: note_code starts at 1 while autocounter starts at 0
    # therefore note_code is actually one less 
    actual_code = key -1 

    if actual_code in self.__patients_notes:
      return self.__patients_notes[actual_code]
    
    # Else, return null
    else:
      return None
    
  def create_note(self, text):
    # Make a new Note object
    current_note = Note(self.__autocounter+ 1, text)
    
    # Store the new Note within patient_notes
    self.__patients_notes[self.__autocounter] = current_note
    
    # Increment autocounter for the next note
    self.__autocounter += 1
    
    # save notes (pickle dump)
    self.save_notes()
    
    return current_note
  
  def save_notes(self):
    if self.autosave:
      with open(self.filename, 'wb') as file2:
          dump(self.__patients_notes, file2)      
    
  def retrieve_notes(self, search_string):
    # Return a list of all the notes that contain the keywords in their contents
    
    list_of_notes = self.__patients_notes.values()
    return_list = []
    
    # look through each note and check if the keyword is within the text
    for note in list_of_notes:
      
      # if keyword is found within the note, append it to the return list
      if search_string in note.get_text():
        return_list.append(note)
    
    return return_list
    
  def update_note(self, key, text):
    # get the wanted note (or try to).
    cur_note = self.search_note(key)
    
    # check if cur_note acutally exist
    if cur_note:
      
      # if cur_note does exist update note and return true
      cur_note.update_text(text)
      
      # save notes (pickle dump)
      self.save_notes()
      return True
    
    # if cur_note doesn't exist (None), return false
    else:
      return False
    
  def delete_note(self, key):
    # if patient have a note with the key, then delete note and return true
    if self.search_note(key):
      self.__patients_notes.pop(key-1)
      
      # save notes (pickle dump)
      self.save_notes()      
      return True
    
    #otherwise do nothing and return False
    else:
      return False
    
  def list_notes(self):
    # return all notes within self.__patients_notes
    list_of_notes = list(self.__patients_notes.values())
    
    # reversing it so we have the list in the order is was added 
    list_reverse = list_of_notes[::-1]
    return list_reverse 