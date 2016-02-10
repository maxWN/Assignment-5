

__name__ = 'db_access.py'
__author__ = 'Max W. Nakel'


import os.path
import sqlite3
conn = sqlite3.connect("measures.sqlite")

def dictionary_factory(cursor, row):
    """
    Create a dictionary from rows in a cursor result.
    The keys will be the column names.
    :param cursor: A cursor from which a query row has just been fetched
    :param row: The query row that was fetched
    :return: A dictionary associating column names to values
    """
    col_names = [d[0].lower() for d in cursor.description]
    return dict(zip(col_names, row))

conn.row_factory = dictionary_factory


def get_all_areas():

    get_all = 'select * from area'
    crsr = conn.cursor()
    exe = crsr.execute(get_all)
    lst0 = exe.fetchall()
    if not lst0:
        return None

    # return exe.fetchall()
    return lst0
    """
    Returns a list of dictionaries representing all the rows in the
    area table.
    """


def get_locations_for_area(area_id):

    get_area = "select * from location where location_area = ?" #+ str(area_id)
    curs = conn.cursor()
    locate = curs.execute(get_area, [area_id]) #2nd argument must be a list data type object!
    # locate = curs.execute(get_area, area_id)
    group = locate.fetchall()
    return group
    """
    Return a list of dictionaries giving the locations for the given area.
    """

def get_measurements_for_location(location_id):

    get_measures = "select value from measurement where measurement_location = ?" #+ str(location_id)
    curs = conn.cursor()
    places = curs.execute(get_measures, [location_id])
    lst = places.fetchall()
    if len(lst) < 1:
        return None
    return lst
    """
    Return a list of dictionaries giving the measurement rows for the given location.
    """


def get_categories_for_area(area_id):

    # lst = []
    get_cat_id = "select category_id from category_area where area_id = ?"
    strike = conn.cursor()
    grab = strike.execute(get_cat_id, [area_id])
    a = grab.fetchall()

    if not a:
        return None

    get_categories = "select * from category where category_id = ?"
    curs = conn.cursor()
    categories = []
    for z in a:
        c = curs.execute(get_categories, [z['category_id']])
        obj = c.fetchall()
        categories += (obj)

    return categories
    """
    Return a list of rows from the category table that all contain the given area.
    """

def get_area_by_id(area_id):
    get = conn.cursor()
    if not area_id:
        return None
    get_area = "select name from area where area_id = ?"
    a = get.execute(get_area, [area_id])

    lst = a.fetchall()
    if not lst:
        return None

    # return a.fetchall()
    return lst
    """
    Return a list of rows from the area table that have the given area_id. This should never have more than one element.
    The list may be empty if area_id is not used by an area entity.
    """

def get_location_by_id(location_id):
    crs = conn.cursor()
    if not location_id:
        return None
    # get_location = "select name from location where location_id = ?"
    get_location = "select * from location where location_id = ?"
    b = crs.execute(get_location, [location_id])

    list2 = b.fetchall()
    ###REMEMBER, whenever the fetchall() function is used, you cannot use the same funciton again because all of the previous results will be gone
    ###The fetchall() funciton retrieves all of the results and stores them in a list. Because all of those values have been appended, they cannont
    ###be retrieved again!
    if not list2:
        return None

    # return b.fetchall()
    return list2

    """
    Return a list of rows from the location table that have the given location_id. This should never have more than one
    element. The list may be empty if location_id is not used by a location entity.
    """




def get_connection():
    # this_dir = split(__file__)[0]
    # fname = join(this_dir, 'sqlite-sakila_1.sq')
    conn = sqlite3.connect("measures.sqlite")
    conn.row_factory = dictionary_factory
    return conn




# import sqlite3
#
# def dict_factory(cursor, row):
#     d = {}
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#     return d
#
# #con = sqlite3.connect(":memory:")
# conn.row_factory = dict_factory
# cur = conn.cursor()
# cur.execute("select 1 as a")
# print(cur.fetchone()["a"])
