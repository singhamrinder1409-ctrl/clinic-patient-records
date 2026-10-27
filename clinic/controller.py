from .patient import * 
from .dao.patient_dao_json import PatientDAOJSON

from .exception.invalid_login_exception import InvalidLoginException
from .exception.duplicate_login_exception import DuplicateLoginException
from .exception.invalid_logout_exception import InvalidLogoutException
from .exception.illegal_access_exception import IllegalAccessException
from .exception.illegal_operation_exception import IllegalOperationException
from .exception.no_current_patient_exception import NoCurrentPatientException

# for password hashing (encrpyting and decrpyting)
import hashlib

class Controller:
  
  def __init__(self, autosave = False):
    self.__login_state = False
    
    # current patient
    self.current_patient = None
    
    # autosave
    self.autosave = autosave
    
    # instantiating PatientDAOJSON 
    self.patient_dao = PatientDAOJSON(self.autosave)    
    
    if not self.autosave:
      # when autosave is off, use the user and password that are hardcoded
      
      # Synthetic coursework/demo accounts only.
      self.login_cred = {'user': '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92', 'ali': '6394ffec21517605c1b426d43e6fa7eb0cff606ded9c2956821c2c36bfee2810'}
    else:
      # when autosave is on, use the user and password that are saved within users.txt
      
      # loop through each line and store the user and their password in login_cred
      file = open("clinic/users.txt", "r")
      self.login_cred = {}
      
      for line in file:
        line = line.strip()
        line = line.split(",")
        
        name, password_hash = line
        self.login_cred[name] = password_hash
        
      file.close()
  
  def login(self, username: str, password: str):
    # if already logged in, throw exception
    if self.__login_state == True:
      raise DuplicateLoginException("cannot login again while still logged in")
    
    # if the username does not match the correct user name, throw exception
    elif username not in self.login_cred:
      raise InvalidLoginException("login in with incorrect username")
    
    # if the password does not match the correct password, throw exception
    elif self.get_password_hash(password) != self.login_cred[username]:
      raise InvalidLoginException("login in with incorrect password")
    
    # if not logged and login credentials are correct, set login status to True
    else:  
      self.__login_state = True
      return True
    
  def get_password_hash(self, password):
      # NOTE: provided in lab9!!!
      encoded_password = password.encode('utf-8')     # Convert the password to bytes
      hash_object = hashlib.sha256(encoded_password)      # Choose a hashing algorithm (e.g., SHA-256)
      hex_dig = hash_object.hexdigest()       # Get the hexadecimal digest of the hashed password
      return hex_dig  
    
  
  def logout(self):
    # If login_state is False (no one is currently logged in), return false
    if self.__login_state != True:
      #return False
      raise InvalidLogoutException("log out only after being logged in")
    else:
      # If login_state is True (someone is logged in), return True and update login_state to False.
    
      self.__login_state = False
      return True
    
  def create_patient(self, phn: int, name: str, birth_date: str, phone: str, email: str, address: str):
    # check if the user is logged in
    if not self.__login_state:
      # if user is not logged in, throw an IllegalAccessException
      raise IllegalAccessException("cannot search patient without logging in")
    
    # check if there is a patient with the same phn
    elif self.search_patient(phn): 
      # if there is a user with the same phn, throw an IllegalOperationException 
      raise IllegalOperationException("cannot add a patient with a phn that is already registered")
    
    else:
      # creating a new patient object
      new_patient = Patient(phn, name, birth_date, phone, email, address, self.autosave)
      return self.patient_dao.create_patient(new_patient) 
    
    
  def search_patient(self, phn: int):
    # check if the user is logged in
    if not self.__login_state:
      # if user is not logged in, throw an IllegalAccessException
      raise IllegalAccessException("cannot search patient without logging in")
    
    else:
      return self.patient_dao.search_patient(phn) 
      
  
  def retrieve_patients(self, name: str):
    # check if the user is logged in
    if not self.__login_state:
      # if user is not logged in, throw an IllegalAccessException
      raise IllegalAccessException("cannot search patient without logging in")
    
    else:
      return self.patient_dao.retrieve_patients(name)
  
  def update_patient(self, wanted: int, phn: int, name: str, birth_date: str, phone: str, email: str, address: str):
    # check if the user is logged in
    if not self.__login_state:
      # if user is not logged in, throw an IllegalAccessException
      raise IllegalAccessException("cannot update patient without logging in")
    
    # if there is a current patient set, then throw an IllegalOperationException
    if self.current_patient:
      raise IllegalOperationException("cannot update the current patient")    
    
    # if wanted is not in the list of patients, then throw an IllegalOperationException
    if not self.search_patient(wanted):
      raise IllegalOperationException("cannot update patient with a phn that is not registered")
     
    # if the user wants to update the patient's phn but new phn already exist, throw an IllegalOperationException.
    if wanted != phn and self.search_patient(phn):
      raise IllegalOperationException("cannot update patient and give them a registered phn")

    # created a new_patient_info which is a patient that contains all the info that the new patient should look like
    new_patient_info = Patient(phn, name, birth_date, phone, email, address, self.autosave)
    return self.patient_dao.update_patient(wanted, new_patient_info)
    
  def delete_patient(self, patients_phn: int):
    # check if the user is logged in
    if not self.__login_state:
      # if user is not logged in, throw an IllegalAccessException
      raise IllegalAccessException("cannot delete patient without logging in")
    
    # if patient_phn == self.current, throwIllegalOperationException
    if patients_phn == self.current_patient:
      raise IllegalOperationException("cannot delete the current patient")
    
    # if the patient does not exist.
    if not self.search_patient(patients_phn):
      raise IllegalOperationException("cannot delete patient with a phn that is not registered")
    
    return self.patient_dao.delete_patient(patients_phn)
    
  def list_patients(self):
    # check if the user is logged in
    if not self.__login_state:
      # if user is not logged in, throw an IllegalAccessException
      raise IllegalAccessException("cannot list patients without logging in")
    
    return self.patient_dao.list_patients()
    
  def get_current_patient(self):
    # check if the user is logged in
    if self.__login_state == False:
      # if user is not logged in, throw an IllegalAccessException
      raise IllegalAccessException("cannot get current patient without logging in")
    
    # If there is a current_patient set, return current patient object 
    if self.current_patient:
      return self.search_patient(self.current_patient)
      
    # If no current_patient, return null. Or not logged in
    else:
      return None
      
  def set_current_patient(self, phn: int):
    # check if the user is logged in
    if self.__login_state == False:
      # if user is not logged in, throw an IllegalAccessException
      raise IllegalAccessException("cannot set current patient without logging in")
    
    # if patient does not exist, throw an IllegalOperationException
    if not self.search_patient(phn):
      raise IllegalOperationException("cannot set non-existent patient as the current patient")
      
    # If there exist a patient with the wanted phn, change the current patient to them.
    self.current_patient = phn
    return self.search_patient(self.current_patient)
      
  def unset_current_patient(self):
    # check if the user is logged in
    if self.__login_state == False:
      # if user is not logged in, throw an IllegalAccessException
      raise IllegalAccessException("cannot unset current patient without logging in")
    
    # Checking if current_patient != Null
    if self.current_patient != None:
      # if current_patient is set, unset current_patient
      self.current_patient = None
      return True
    else:
      return False
      
  def create_note(self, note_content: str):
    # check if the user is logged in
    if self.__login_state == False:
      # if user is not logged in, throw an IllegalAccessException
      raise IllegalAccessException("cannot add note for a patient without logging in")
    
    # if there isn't a current_patient set, throw a NoCurrentPatientException
    if self.current_patient == None:
      raise NoCurrentPatientException("cannot add note without a valid current patient")
        
    # get current patient object
    patient = self.search_patient(self.current_patient)

    # call its add_note() method
    new_note = patient.add_note(note_content)
    return new_note
  
  
  def search_note(self, note_code: int):
    # check if the user is logged in
    if self.__login_state == False:
      # if user is not logged in, throw an IllegalAccessException
      raise IllegalAccessException("cannot search note for a patient without logging in")
    
    # if there isn't a current_patient set, throw a NoCurrentPatientException
    if self.current_patient == None:
      raise NoCurrentPatientException("cannot search note without a valid current patient")

    # Get current patient object within dictionary
    cur_patient = self.search_patient(self.current_patient)

    # Call patient's have_note() method
    return cur_patient.have_note(note_code)
    
  def retrieve_notes(self, key_words: str):
    # check if the user is logged in
    if self.__login_state == False:
      # if user is not logged in, throw an IllegalAccessException
      raise IllegalAccessException("cannot retrieve note for a patient without logging in")
    
    # if there isn't a current_patient set, throw a NoCurrentPatientException
    if self.current_patient == None:
      raise NoCurrentPatientException("cannot retrieve note without a valid current patient")
    
    # Get patient record class
    cur_patient = self.search_patient(self.current_patient)
    
    # Calling patient's notes_with_keywords() to get a list of all the notes with the wanted keywords.
    # NOTE: if there are no notes with the wanted keywords, an empty list will be returned
    list_of_wanted_notes = cur_patient.notes_with_keyword(key_words)
    return list_of_wanted_notes
  

  def update_note(self, wanted_note_code: int, new_text:str):
    # check if the user is logged in
    if self.__login_state == False:
      # if user is not logged in, throw an IllegalAccessException
      raise IllegalAccessException("cannot retrieve note for a patient without logging in")
    
    # if there isn't a current_patient set, throw a NoCurrentPatientException
    if self.current_patient == None:
      raise NoCurrentPatientException("cannot retrieve note without a valid current patient")
      
    # Get current patient object within dictionary
    cur_patient = self.search_patient(self.current_patient)
    
    # Calling patient's update_patient_notes()
    return cur_patient.update_patient_notes(wanted_note_code, new_text)
  
  def delete_note(self, note_code: int):
    # check if the user is logged in
    if self.__login_state == False:
      # if user is not logged in, throw an IllegalAccessException
      raise IllegalAccessException("cannot delete note for a patient without logging in")
    
    # if there isn't a current_patient set, throw a NoCurrentPatientException
    if self.current_patient == None:
      raise NoCurrentPatientException("cannot delete note without a valid current patient")
    
    # Get current patient object within dictionary
    cur_patient = self.search_patient(self.current_patient)
    
    # if their record contain the wanted note, it'll be delete and True will be returned
    # if their record does not contain the wanted note, nothing will be deleted and False will be returned
    return cur_patient.delete_patient_note(note_code)
  
  def list_notes(self):
    # check if the user is logged in
    if self.__login_state == False:
      # if user is not logged in, throw an IllegalAccessException
      raise IllegalAccessException("cannot list notes for a patient without logging in")
    
    # if there isn't a current_patient set, throw a NoCurrentPatientException
    if self.current_patient == None:
      raise NoCurrentPatientException("cannot list notes without a valid current patient")
  
    # Get current patient object within dictionary
    cur_patient = self.search_patient(self.current_patient)
    
    # Return all the notes within patient record 
    # NOTE: if there are no notes, an empty list will be returned
    return cur_patient.list_of_notes()
    
    
    
      
      
    
  
    