"""Run a synthetic, in-memory patient and note workflow."""
from clinic.controller import Controller

controller = Controller(autosave=False)
controller.login("user", "123456")
patient = controller.create_patient(1000000000, "Demo Patient", "2000-01-01", "250-555-0100", "demo@example.com", "Example address")
controller.set_current_patient(1000000000)
controller.create_note("Synthetic example: follow-up appointment requested.")
print("Patient:", patient.get_name())
print("Patients:", len(controller.list_patients()))
print("Notes:", len(controller.list_notes()))
print("Latest note:", controller.list_notes()[0].get_text())
controller.logout()
