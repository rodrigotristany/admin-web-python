import unittest

from owner.models import Owner


class OwnerTestCase(unittest.TestCase):
    def test_string_representation(self):
        my_name = 'Rodrigo'
        instance = Owner(first_name=my_name)
        self.assertEqual(str(instance), f"Hola {my_name}!")


if __name__ == '__main__':
    unittest.main()
