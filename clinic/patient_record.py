from .note import *
from .dao.note_dao_pickle import NoteDAOPickle

class PatientRecord:
  def __init__(self, patient_phn: int, autosave = False): 
    self.autosave = autosave
    self.patient_phn = patient_phn
    
    self.note_pickle = NoteDAOPickle(self.patient_phn, self.autosave)
  
  def new_note(self, text: str): 
    # call note_pickkle to make new notes
    return self.note_pickle.create_note(text)
  
  def update_note_in_record(self, wanted_note_code: int, new_text:str):
    # call note_pickkle to update wanted note
    return self.note_pickle.update_note(wanted_note_code, new_text)
    
  def get_note(self, note_code: int):
    # calling search_note() within note_pickle
    return self.note_pickle.search_note(note_code)
    
  def keywords_lookup(self, keywords: int):
    # calling note_pickle to retrieve all the notes with the keywords
    return self.note_pickle.retrieve_notes(keywords)
  
  def delete_note(self, note_code: int):
    # calling note_pickle.delete_note()
    return self.note_pickle.delete_note(note_code)
    
  def all_notes(self):
    # calling note_pickle.list_notes()
    return self.note_pickle.list_notes()
    
  