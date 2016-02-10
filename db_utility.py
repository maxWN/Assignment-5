
__name__ = 'db_utility.py'
__author__ = 'Max W. Nakel'

import math
import sqlite3
from db_access import get_measurements_for_location, get_locations_for_area
conn = sqlite3.connect("measures.sqlite")

from db_access import get_all_areas

def get_average_measurements_for_area(area_id):

    rVal = 0
    id = get_locations_for_area(area_id)
    if not id:
        return None
    lst = []
    for z in id:
        lst.append(z['location_id'])
    if not lst:
        return None
    summe = []
    three = []
    for r in lst:
        summe = (get_measurements_for_location(r))
        if summe:
            three += (summe)

    sum = 0
    total = len(three)
    for e in three:
        sum += e['value']
    rVal = sum/total
    return rVal

    """
    Returns the average value of all measurements for all locations in the given area.
    Returns None if there are no measurements.
    """

def number_of_locations_by_area(area_id):
    id = get_locations_for_area(area_id)
    num = len(id)
    # print(num)
    return num
    """
    Returns the number of locations for the given area.
    """


