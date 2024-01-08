#!/usr/bin/python3

__author__ = 'Max W. Nakel'

import cgi
import cgitb
from db_access import get_locations_for_area, get_categories_for_area, get_all_areas, get_measurements_for_location, get_area_by_id
from db_utility import number_of_locations_by_area, get_average_measurements_for_area

cgitb.enable()

print("Content-Type:text/html; charset=UTF-8")
# print("Content-Type: html/text; charset: UTF-8")
print()

collect = cgi.FieldStorage()
user_val = collect.getfirst("area_id")

print("""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="/assign_five/style1.css" rel="stylesheet" type="text/css">
<link rel="icon" href="/assign_five/Bokehlicia-Captiva-File-manager.ico">
<!--script src="/jquery-1.11.3.js" type="text/javascript"></script-->
<title>Assignment 5</title>
</head>
    <body>
        <div id="main_content_area">
            <div id="main_title_navbar">
                <div id="title_space">Internet Programming: Assignment 5</div>
                <div class="link_cells link_cell_top"><a href="/assign_five/a5_home_page.html">Home Page</a></div>
                <div class="link_cells link_cell_center"><a href="/cgi-bin/area_table.py">Display all Areas</a></div>
                <div class="link_cells link_cell_bottom"><a href="/assign_five/a5_error_testing_page.html">Error Testing</a></div>
                <div id="symbol_space">
                   <img src="/assign_five/5Cubes2.png" height="150px" width="150px"/>
                </div>
            </div>""")

bool = True
# numeric = int(user_val)
if user_val != None:
    for abc in user_val:
        if abc.isdigit() == False:
            bool = False
            # print(abc)

# if user_val != None and type(user_val) != int:
if user_val != None and bool:
    val = get_area_by_id(user_val)

    if val == None: #lines 44-49 will detect if a user has submitted a value which can't be found within the database
        a = get_all_areas()
        print("<div id=\"error_page1\"><strong>ERROR: User entered an ID which was not found!</strong></br>Select an Area</br><form method=\"get\" action=\"/cgi-bin/location_table.py\"><select name=\"area_id\" size=\"5\"></div>")
        for x in a:
            print("<option value=\"" + str(x['area_id']) + "\">" + x['name'] + "</option>")
        print("</select></br><input id=\"sButton\" type=\"submit\" value=\"Submit\"></form></div></div></body></html>")

    else:
        # print("test", val)
        for a in val:
            print("<div id=\"page_body2\">Location Information for the " + a['name'] + " area </br></br>")
        print("<form method =\"get\" action=\"/cgi-bin/measurement_table.py\"><table class=\"grid\"><th class=\"grid\">Select</th><th class=\"grid\">ID</th><th class=\"grid\">Name</th><th class=\"grid\">Altitude</th>")
        for x in get_locations_for_area(user_val):
            # print("<tr> <td><input type=\"radio\" value=\"" + x['name'] + "\" name=\"" + x['name'] + "\"></td> <td>" + str(x['location_id']) + " </td> <td>" + x['name'] + " </td> <td>" + str(x['altitude']) + " </td> </tr>")
            print("<tr> <td><input type=\"radio\" value=\"" + str(x['location_id']) + "\" name=\"location_id\"></td> <td>" + str(x['location_id']) + " </td> <td>" + x['name'] + " </td> <td>" + str(x['altitude']) + " </td> </tr>")

        print("</table></br><input id=\"sButton\" type=\"submit\"></form></div></body></html>")


elif user_val == None: #lines 63-68 will detect if a user hasn't subimtted any data
    a = get_all_areas()
    print("<div id=\"error_page1\"><strong>ERROR: User did not make a valid selection.</strong></br>Select an Area</br><form method=\"get\" action=\"/cgi-bin/location_table.py\"><select name=\"area_id\" size=\"5\"></div>")
    for x in a:
        print("<option value=\"" + str(x['area_id']) + "\">" + x['name'] + "</option>")
    print("</select></br><input id=\"sButton\" type=\"submit\" value=\"Submit\"></form></div></div></body></html>")

# elif type(user_val) == int: #lines 70-75 will detect if a user has submitted an integer value instead of a string
elif bool == False: #lines 70-75 will detect if a user has submitted an integer value instead of a string
    a = get_all_areas()
    print("<div id=\"error_page1\"><strong>ERROR: User selected data that was not of integer data type.</strong></br>Select an Area</br><form method=\"get\" action=\"/cgi-bin/location_table.py\"><select name=\"area_id\" size=\"5\"></div>")
    for x in a:
        print("<option value=\"" + str(x['area_id']) + "\">" + x['name'] + "</option>")
    print("</select></br><input id=\"sButton\" type=\"submit\" value=\"Submit\"></form></div></div></body></html>")


