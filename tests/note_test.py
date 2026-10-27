import unittest
from clinic.note import Note
from datetime import date

class TestNote(unittest.TestCase):

    def setUp(self):
        self.fixed_date = date(2024, 11, 4).strftime('%B %d, %Y')
        self.another_date = date(2024, 11, 5).strftime('%B %d, %Y')
        
        self.note1 = Note(code=1, text='Patient is recovering well.')
        self.note1._Note__date_written = self.fixed_date
        
        self.note2 = Note(code=1, text='Patient is recovering well.')
        self.note2._Note__date_written = self.fixed_date
        
        self.note3 = Note(code=2, text='Patient needs further tests.')
        self.note3._Note__date_written = self.another_date

    def test_note_equality(self):
        self.assertTrue(
            self.note1 == self.note2,
        )
        self.assertFalse(
            self.note1 == self.note3,
        )

    def test_note_equality_after_update(self):
    
        self.note2.update_text('Updated note text.')
        self.note2._Note__date_written = self.fixed_date
        
        self.assertFalse(
            self.note1 == self.note2,
        )

    def test_note_equality_with_none(self):
        self.assertFalse(
            self.note1 == None,
        )

if __name__ == '__main__':
    unittest.main()