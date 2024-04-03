from unittest import TestCase, main
from validate_nfe_key import GenerateNfeDV

'''
GenerateNfeDV('3524030555538200013355010000491845106212768')
GenerateNfeDV('3219110557071400082555001005914662113308296')
GenerateNfeDV('3524 0305 5553 8200 0133 5501 0000 4918 4510 6212 768')
GenerateNfeDV('3524.0305.5553.8200.0133.5501.0000.4918.4510.6212.768')
'''


class ValidateNfeKeyTests(TestCase):
    def test_generate_dv(self):
        self.assertEqual(GenerateNfeDV.generate_dv('4317120736461700013555000000012014100012014'), 6)


if __name__ == '__main__':
    main(verbosity=2, )
