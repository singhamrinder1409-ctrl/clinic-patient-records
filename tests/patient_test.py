import unittest
from clinic.patient import Patient

class TestPatient(unittest.TestCase):

    def setUp(self):
        
        self.patient1 = Patient(
            phn='1234567890',
            name='Sananth Badhran',
            birth_date='1990-01-01',
            phone='555-1234',
            email='san@gmail.com',
            address='123 carey rd'
        )
        self.patient2 = Patient(
            phn='1234567890',
            name='Sananth Badhran',
            birth_date='1990-01-01',
            phone='555-1234',
            email='san@gmail.com',
            address='123 carey rd'
        )
        self.patient3 = Patient(
            phn='0987654321',
            name='Aleah james',
            birth_date='1985-05-15',
            phone='555-5678',
            email='aleah@gmail.com',
            address='456 Elm St'
        )

    def test_patient_equality(self):
        self.assertTrue(
            self.patient1 == self.patient2,
        )
        self.assertFalse(
            self.patient1 == self.patient3,
        )

    def test_patient_str(self):

        expected_str = "Patient's name is Sananth Badhran"
        self.assertEqual(
            str(self.patient1),
            expected_str,
        )

    def test_patient_equality_with_none(self):
        self.assertFalse(
            self.patient1 == None,
        )

if __name__ == '__main__':
    unittest.main()