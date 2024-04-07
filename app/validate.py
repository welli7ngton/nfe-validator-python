# flake8: noqa
from typing import List

import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from my_exceptions.exceptions import InvalidNFEKeyLength


class GenerateNfeDV:  
    @classmethod
    def generate_dv(cls, nfe_number) -> int | None:
        if ' ' in nfe_number:
            nfe_number = cls.remove_white_space(nfe_number)
        
        if '.' in nfe_number:
            nfe_number = cls.remove_dot(nfe_number)

        if cls.verify_nfe_len(nfe_number):
            nfe_number_int = cls.generate_list_of_int(nfe_number)
            numbers_to_mulitplication = cls.reverse_list(cls.generate_numbers_to_multiplication(nfe_number_int))
            sum_of_list_items = cls.get_sum_of_lists_multiplications(nfe_number_int, numbers_to_mulitplication)
            return cls.get_DV(sum_of_list_items)
        else:
            raise InvalidNFEKeyLength(len(nfe_number))

    @classmethod
    def verify_nfe_len(cls, nfe_number: str) -> bool:
        return len(nfe_number) == 43

    @classmethod
    def generate_list_of_int(cls, _list: List[str]) -> List[int]:
        return [int(n) for n in _list]

    @classmethod
    def reverse_list(cls, _list: List[int]) -> List[int]:
        return _list[len(_list)::-1]

    @classmethod
    def generate_numbers_to_multiplication(cls, nfe_numbers: List[int]) -> List[int]:
        counter = 2
        numbers_multiplication = []
        for i in range(len(nfe_numbers), 0, -1):
            if counter == 10:
                counter = 2
                pass
            numbers_multiplication.append(counter)
            counter += 1
        return numbers_multiplication

    @classmethod
    def get_sum_of_lists_multiplications(cls, _list1: List[int], _list2: List[int]) -> int:
        return sum([_list1[i] * _list2[i] for i in range(len(_list1))])

    @classmethod
    def get_DV(cls, sum_of_lists: int) -> int:
        print(sum_of_lists)
        DV = 11 - (sum_of_lists % 11)
        return DV if DV <= 9 else 0
    
    @classmethod
    def remove_white_space(cls, nfe_number: str) -> str:
        return "".join([char for char in nfe_number if char != ' '])
    
    @classmethod
    def remove_dot(cls, nfe_number: str) -> str:
        return "".join([char for char in nfe_number if char != '.'])   
