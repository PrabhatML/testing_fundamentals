from unittesting.func.employee import Employee
import unittest
from unittest.mock import patch

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass    

    # Run before every test
    def setUp(self) -> None:
        self.emp1 = Employee("Prabhat","Sharma",50000)
        self.emp2 = Employee("Rahul","Pareek",44000)

    # Run after every test
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_email(self):

        self.assertEqual(self.emp1.email,'Prabhat.Sharma@email.com')
        self.assertEqual(self.emp2.email,"Rahul.Pareek@email.com")

        self.emp1.first = "Ravi"
        self.emp2.first = "Viru"

        self.assertEqual(self.emp1.email,'Ravi.Sharma@email.com')
        self.assertEqual(self.emp2.email,"Viru.Pareek@email.com")

    def test_fullname(self):


        self.assertEqual(self.emp1.fullname,"Prabhat Sharma")
        self.assertEqual(self.emp2.fullname,"Rahul Pareek")

        self.emp1.first = "Ravi"
        self.emp2.first = "Viru"

        self.assertEqual(self.emp1.fullname,"Ravi Sharma")
        self.assertEqual(self.emp2.fullname,"Viru Pareek")

    def test_salary(self):

        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay,52500)
        self.assertEqual(self.emp2.pay,46200)


    # Mocking
    def test_monthly_schedule(self):
        with patch('unittesting.func.employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp1.monthly_schedule("May")
            mocked_get.assert_called_once_with("http://company.com/Sharma/May")
            self.assertEqual(schedule,"Success")


            mocked_get.return_value.ok = False
            mocked_get.return_value.text = "Bad Response!"

            schedule = self.emp2.monthly_schedule("June")
            mocked_get.assert_called_with("http://company.com/Pareek/June")
            self.assertEqual(schedule,"Bad Response!")

"""
setUp() / tearDown()` – before and after test methods
setUpClass() / tearDownClass() – before and after a class of tests
setUpModule() / tearDownModule() – before and after a module of tests
"""