from .patient_record import *

class Patient:
  def __init__(self, phn, name, birth_date, phone, email, address, autosave = False): 
    self.__phn = phn
    self.__name = name
    self.__birth = birth_date
    self.__phone = phone
    self.__email = email
    self.__address = address
    
    self.autosave = autosave
    self.__record = PatientRecord(self.__phn, self.autosave)
    
  def __eq__ (self, other):
    
    if other == None:
      return False
    else:
      return self.__phn == other.__phn and self.__name == other.__name and self.__birth == other.__birth and self.__phone == other.__phone and self.__email == other.__email and self.__address == other.__address
   
  def get_address(self):
    return self.__address
  
  def get_email(self):
    return self.__email
  
  def get_phone(self):
    return self.__phone
  
  def get_birth_date(self):
    return self.__birth
  
  def __str__(self):
    return f'Patient\'s name is {self.__name}'
  
  def __repr__(self):
    return f'PHN: {self.__phn}, NAME: {self.__name}, BIRTH: {self.__birth}, PHONE: {self.__phone}, EMAIL: {self.__email}, ADDRESS: {self.__address}'
  
  def change_phn(self, phn: int):
    self.__phn = phn
    
  def get_phn(self):
    return self.__phn  
    
  def get_name(self):
    return self.__name
  
  def change_name(self, name: str):
    self.__name = name
    
  def change_birth(self, birth_date: str):
    self.__birth = birth_date 
    
  def change_phone(self, phone: str):
    self.__phone = phone    
    
  def change_email(self, email: str):
    self.__email = email
    
  def change_address(self, address: str):
    self.__address = address
    
  def get_record(self):
    return self.__record
  
  def add_note(self, text: str):
    return self.__record.new_note(text)
  
  def have_note(self, code: int):
    return self.__record.get_note(code)
  
  def notes_with_keyword(self, key_words: str):
    return self.__record.keywords_lookup(key_words)
  
  def update_patient_notes(self, wanted_note_code: int, new_text:str):
    return self.__record.update_note_in_record(wanted_note_code, new_text)
  
  def delete_patient_note(self, note_code: int):
    return self.__record.delete_note(note_code)
  
  def list_of_notes(self):
    return self.__record.all_notes()
    
  