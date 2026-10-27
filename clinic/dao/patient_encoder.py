import json
#from ..patient import Patient
from clinic.patient import Patient

class PatientEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Patient):
            # save patient's phn, name, birth, phone, email, address, and autosave (if they want to save their info).
            # NOTE: We're saving self.autosave because the patient class is passing autosave to patient_record which also passes to note_dao_pickle.
            
            return {"__type__": "Patient", "__phn": int(obj.get_phn()), "__name": obj.get_name(), "__birth": obj.get_birth_date(), "__phone":obj.get_phone(), "__email":obj.get_email(), "__address": obj.get_address(), "autosave":obj.autosave }
        
        return super().default(obj)