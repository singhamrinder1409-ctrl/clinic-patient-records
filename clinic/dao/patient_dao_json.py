from .patient_dao import * 
from .patient_encoder import * 
from .patient_decoder import * 

class PatientDAOJSON(PatientDAO):
    def __init__(self, autosave = False):
        
        # fields used for json
        self.autosave = autosave
        
        # the location where all patients are stored if autosave is turned on
        self.filename = 'clinic/patients.json'
        
        self.list_of_patients = {}
        
        # if autosave is on, read the list_of_patients from patients.json
        self.load_patients()
        
    def load_patients(self):
        # if autosave is on, read the list_of_patients from patients.json
        if self.autosave:
            try:
                with open(self.filename, 'r') as file:
                    json_data = file.read()
                    self.list_of_patients = json.loads(json_data, cls = PatientDecoder)
                    file.close()
            except:
                pass
            
            # Remake the dictionary. Since json stores the dictionary keys as strings, we have to reread each dictionary entry and store them with an int key.
            temp = {}
            
            for item in list(self.list_of_patients.items()):
                key, value = item 
                temp[int(key)] = value
                
            self.list_of_patients = temp         
        
    
    def search_patient(self, phn: int):
        # Return the patient object, if there exist a patient with the same phn within list_of_patient.
        
        #print(phn in self.list_of_patients)
        if phn in self.list_of_patients:
            return self.list_of_patients[phn]
        
        # else, return null
        else:
            return None     
        
    def create_patient(self, new_patient):
        # adding patient object to list_of_patient with their phn as their key
        self.list_of_patients[new_patient.get_phn()] = new_patient
        
        # if autosave is on, save patient within patient.json
        self.update_json_file()
        
        # return pointer to the new patient object
        return new_patient 
    
    def update_json_file(self):
        # if autosave is on, update patient.json file with new list_of_patient
        if self.autosave:
            with open(self.filename, 'w') as file:
                # encode list_of_patient according to PatientEncoder and save the encryption in json format within self.filename
                json_data = json.dumps(self.list_of_patients, cls = PatientEncoder)
                file.write(json_data)
                file.close()        
    
    def retrieve_patients(self, search_string):
        # will hold all the patients with the same name
        return_list = []
        
        # loops through the values of list_of_patients
        for person in self.list_of_patients.values():
            # checks if they have the same name
            if search_string in person.get_name():
              
                # if same name, append to the return list 
                return_list.append(person)
          
        # return a list of all the patients with the same name
        return return_list
    
    
    def update_patient(self, key, patient):
        # NOTE: patient is a container of all the changes that should be made
        
        # if user wanted to change the wanted's phn
        patient_phn = patient.get_phn()
        
        if key != patient_phn:
            self.list_of_patients[key].change_phn(patient_phn)
            self.list_of_patients[patient_phn] = self.list_of_patients.pop(key)  
            key = patient_phn
          
        wanted_person = self.list_of_patients[key]  
          
        # update the wanted patient field with the patient info
        wanted_person.change_name(patient.get_name())
        wanted_person.change_birth(patient.get_birth_date())
        wanted_person.change_phone(patient.get_phone())
        wanted_person.change_email(patient.get_email())
        wanted_person.change_address(patient.get_address())
        
        # if autosave is on, save the updated patient within patient.json
        self.update_json_file()
        
        return True
    
    def delete_patient(self, key):
        # Remove patient from list_of_patient
        self.list_of_patients.pop(key)
        
        # if autosave is on, save the changes made to list_of_patients
        self.update_json_file()
        return True
    
    def list_patients(self):
        # return the patients within list_of_patient
        return list(self.list_of_patients.values())