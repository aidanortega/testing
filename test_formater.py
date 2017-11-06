from unittest import TestCase
from main import Formater
import sys
sys.tracebacklimit = 0

class TestFormater(TestCase):
    def setUp(self):
        print(self._testMethodDoc)

    def tearDown(self):
        pass

    def test_clean_integers(self):
        """-- Test Clean Integers --"""
        msg = "The correct numerical value is not being returned (Int)"

        self.assertEqual(Formater.clean_number('9, 000 000'), 9000000, msg = msg)
        self.assertEqual(Formater.clean_number('5'), 5, msg = msg)
        self.assertEqual(Formater.clean_number('58, 710, 520'), 58710520, msg = msg)

    def test_correct_int_cast(self):
        """-- Test Correct Int Cast --"""
        self.assertIsInstance(Formater.clean_number('9, 000 000'), int)
        self.assertIsInstance(Formater.clean_number('5'), int)
        self.assertIsInstance(Formater.clean_number('58, 710, 520'), int)

    def test_clean_floats(self):
        """-- Test Clean Floats --"""
        msg = "The correct numerical value is not being returned (Float)"

        self.assertEqual(Formater.clean_number('9.9'), 9.9, msg = msg)
        self.assertEqual(Formater.clean_number('9, 000.9'), 9000.9, msg = msg)

    def test_correct_float_cast(self):
        """-- Test Correct Float Cast --"""
        self.assertIsInstance(Formater.clean_number('9.9'), float)
        self.assertIsInstance(Formater.clean_number('9, 000.9'), float)

    def test_comma_after_dot(self):
        """-- Test Comma After Dot"""
        self.assertEqual(Formater.clean_number('7, 000.000,000'), None)

    def test_multiple_dots(self):
        """-- Test Multiple Dots"""
        self.assertEqual(Formater.clean_number("7.000.000"), None)

    def test_no_valid_entrys(self):
        """-- Test No Valid Entrys"""
        self.assertEqual(Formater.clean_number("hola"), None)