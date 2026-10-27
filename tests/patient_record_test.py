import unittest
from clinic.patient_record import PatientRecord
from clinic.note import Note

class TestPatientRecord(unittest.TestCase):
    def setUp(self):
        self.patient_record = PatientRecord(1000000000)

    def test_add_and_get_notes(self):
    
        note1 = self.patient_record.new_note("Patient has a sore throat")
        note2 = self.patient_record.new_note("Prescribed medication")
        self.assertEqual(note1.get_text(), "Patient has a sore throat", "First note text should match")
        self.assertEqual(note2.get_text(), "Prescribed medication", "Second note text should match")

        retrieved_note1 = self.patient_record.get_note(1)
        retrieved_note2 = self.patient_record.get_note(2)
        self.assertEqual(retrieved_note1, note1, "Retrieved first note should match the original")
        self.assertEqual(retrieved_note2, note2, "Retrieved second note should match the original")

    def test_update_note(self):
        self.patient_record.new_note("Initial diagnosis")

        update_success = self.patient_record.update_note_in_record(1, "Revised diagnosis")
        self.assertTrue(update_success)

        updated_note = self.patient_record.get_note(1)
        self.assertEqual(updated_note.get_text(), "Revised diagnosis", "Note text should be updated")

    def test_delete_note(self):
        self.patient_record.new_note("Note to be removed")

        delete_success = self.patient_record.delete_note(1)
        self.assertTrue(delete_success)

        deleted_note = self.patient_record.get_note(1)
        self.assertIsNone(deleted_note)

    def test_keywords_lookup(self):
        
        self.patient_record.new_note("Patient complains about headaches")
        self.patient_record.new_note("headaches have increased since last visit")
        self.patient_record.new_note("Patient is not feeling better overall")

        search_results = self.patient_record.keywords_lookup("headaches")
        self.assertEqual(len(search_results), 2, "Should find two notes containing 'headaches'")

        result_texts = [note.get_text() for note in search_results]
        self.assertIn("Patient complains about headaches", result_texts)
        self.assertIn("headaches have increased since last visit", result_texts)

    def test_all_notes_order(self):
        self.patient_record.new_note("First note")
        self.patient_record.new_note("Second note")
        self.patient_record.new_note("Third note")

        all_notes = self.patient_record.all_notes()
        self.assertEqual(len(all_notes), 3,"Should have three notes in total")
        self.assertEqual(all_notes[0].get_text(),"Third note", "Latest note should be first")
        self.assertEqual(all_notes[1].get_text(), "Second note")
        self.assertEqual(all_notes[2].get_text(), "First note", "Earliest note should be last")


if __name__ == '__main__':
    unittest.main()