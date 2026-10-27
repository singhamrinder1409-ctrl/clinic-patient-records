from json import JSONDecoder
from clinic.patient import Patient

class PatientDecoder(JSONDecoder):
  def __init__(self, *args, **kwargs):
    super().__init__(object_hook=self.object_hook, *args, **kwargs)

  def object_hook(self, dct):
    # load patient's phn, name, birth, phone, email, address, and autosave (if they want to save their info).
    
    if "__type__" in dct and dct["__type__"] == "Patient":
      return Patient(int(dct["__phn"]), dct["__name"], dct["__birth"], dct["__phone"], dct["__email"], dct["__address"], dct["autosave"])
    return dct
