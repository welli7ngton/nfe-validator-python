# flake8: noqa

import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))


from unittest import TestCase, main

from app.validate import GenerateNfeDV
from my_exceptions.exceptions import InvalidNFEKeyLength

class ValidateNfeKeyTests(TestCase):
    def test_generate_dv(self):
        self.assertEqual(GenerateNfeDV.generate_dv('4317120736461700013555000000012014100012014'), 6)

    def test_nfe_length_get_an_exception(self):
        with self.assertRaises(InvalidNFEKeyLength):
            GenerateNfeDV.generate_dv('43171207364617000135550000000120141000120144')
    
    def test_remove_white_space(self):
        assert '1111' == GenerateNfeDV.remove_white_space(' 1 1 1 1 ')

    def test_remove_dot(self):
        assert '1111' == GenerateNfeDV.remove_dot('1.1.1.1.')
    
    def test_generate_a_list_of_int(self):
        assert [1, 1, 1, 1] == GenerateNfeDV.generate_list_of_int(['1', '1', '1', '1'])
    
    def test_reverse_list(self):
        assert [4, 3, 2, 1] == GenerateNfeDV.reverse_list([1, 2, 3, 4])
    
    def test_generate_numbers_to_multiplication(self):
        nfe_number_test = '4317120736461700013555000000012014100012014'
        result_expected = [
            2, 3, 4, 5, 6, 7, 8,
            9, 2, 3, 4, 5, 6, 7,
            8, 9, 2, 3, 4, 5, 6,
            7, 8, 9, 2, 3, 4, 5,
            6, 7, 8, 9, 2, 3, 4,
            5, 6, 7, 8, 9, 2, 3,
            4,
        ]
        assert result_expected == GenerateNfeDV.generate_numbers_to_multiplication(nfe_number_test)
    
    def test_sum_of_lists_multiplications(self):
        assert 8 == GenerateNfeDV.get_sum_of_lists_multiplications([1, 1, 1, 1], [2, 2, 2, 2])
    
    def test_get_dv(self):
        assert 0 == GenerateNfeDV.get_DV(11)
        assert 6 == GenerateNfeDV.get_DV(489)

if __name__ == '__main__':
    main(verbosity=2, )
