import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_division(self):
        assert self.calc.division(self, 15, 5) == 3

    def test_subtraction(self):
        assert self.calc.subtraction(self, 7, 2) == 5
    def test_adding(self):
        assert self.calc.adding(self, 4, 6) == 10




    def teardown(self):
       print("Выполнение метода Teardown")







