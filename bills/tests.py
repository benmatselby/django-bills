from django.test import TestCase

from .models import EnergyBill
from .models import Type


class TestType(TestCase):
    def test_str(self):
        type = Type(handle="electricity", description="Electricity")
        self.assertEqual(str(type), "electricity")


class TestBill(TestCase):
    def test_str(self):
        type = Type(handle="electricity", description="Electricity")
        bill = EnergyBill(
            type=type,
            date_start="2024-12-01 00:00:00",
            date_end="2024-12-31 23:59:59",
            cost=1000,
        )

        self.assertEqual(
            str(bill), "electricity - 2024-12-01 00:00:00 - 2024-12-31 23:59:59 - 1000"
        )
