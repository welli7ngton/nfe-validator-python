# flake8: noqa

from unittest import TestCase, main

from validate_nfe_key import GenerateNfeDV

from exceptions import InvalidNFEKeyLenght


class ValidateNfeKeyTests(TestCase):
    def test_generate_dv(self):
        self.assertEqual(GenerateNfeDV.generate_dv('4317120736461700013555000000012014100012014'), 6)

    def test_nfe_len_get_an_exception(self):
        with self.assertRaises(InvalidNFEKeyLenght) as ex:
            GenerateNfeDV.generate_dv('43171207364617000135550000000120141000120144')


if __name__ == '__main__':
    main(verbosity=2, )
