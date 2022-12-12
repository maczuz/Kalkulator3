from main import kalkulator
import unittest


class TestStringMethods(unittest.TestCase):

    def test_kalkulator_suma(self):
        # given
        a = 4
        b = 2
        expected_suma = 6
        # when
        result_suma = kalkulator(a, b, "suma")
        # then
        self.assertEqual(result_suma, expected_suma)

    def test_kalkulator_roznica(self):
        # given
        a = 4
        b = 2
        expected_roznica = 2
        # when
        result_roznica = kalkulator(a, b, "roznica")
        # then
        self.assertEqual(result_roznica, expected_roznica)

    def test_kalkulator_iloraz(self):
        # given
        a = 4
        b = 2
        expected_iloraz = 2
        # when
        result_iloraz = kalkulator(a, b, "iloraz")
        # then
        self.assertEqual(result_iloraz, expected_iloraz)

    def test_kalkulator_iloczyn(self):
        # given
        a = 4
        b = 2
        expected_iloczyn = 8
        # when
        result_iloczyn = kalkulator(a, b, "iloczyn")
        # then
        self.assertEqual(result_iloczyn, expected_iloczyn)

    def test_kalkulator_typ(self):
        # given
        a = 4
        b = 2
        expected_typ = int
        # when
        result_typ = type(a)
        # then
        self.assertEqual(result_typ, expected_typ)

    def test_kalkulator_typ(self):
        # given
        a = 4
        b = 2
        expected_typ = int
        # when
        result_typ = type(b)
        # then
        self.assertEqual(result_typ, expected_typ)

    def test_kalkulator_typ(self):
        # given
        a = 4
        b = 2
        dzialanie = "suma"
        expected_typ = int
        # when
        result_typ = kalkulator(a, b, dzialanie)
        # then
        self.assertEqual(type(result_typ), expected_typ)


if __name__ == '__main__':
    unittest.main()
