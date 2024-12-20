from django.test import TestCase

from .models import Bill, Type


class TestType(TestCase):
    def test_str(self):
        type = Type(handle="electricity", description="Electricity")
        self.assertEqual(str(type), "electricity")
