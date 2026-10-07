from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.urls import reverse

from .models import Employee


class EmployeeModelTest(TestCase):

    def test_employee_creation(self):
        employee = Employee.objects.create(
            name="Bharathi",
            email="bharathi@example.com",
            phone="9876543210",
            department="IT",
            salary=30000
        )

        self.assertEqual(employee.name, "Bharathi")
        self.assertEqual(employee.department, "IT")


class HomePageTest(TestCase):

    def test_home_page(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
