# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 20:14:46 2022

@author: User
"""

import unittest
from city_functions import *

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        name = city_country('santiago', 'chile')
        self.assertEqual(name, "Santiago,Chile")
    def city_country(city, country, population):
        output_string = f"{city.title()}, {country.title()}"
        output_string += f" -population {population}"
        return output_string
        
if __name__ == '__main__':
    unittest.main()
