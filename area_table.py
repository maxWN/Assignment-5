#!/usr/bin/python3

__author__ = 'Max W. Nakel'

import cgi
import cgitb
from db_access import get_categories_for_area, get_measurements_for_location, get_all_areas, get_area_by_id, get_location_by_id, get_locations_for_area
from db_utility import get_average_measurements_for_area, number_of_locations_by_area

cgitb.enable()

print("Content-Type:text/html; charset=UTF-8")
print()

print("""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="/assign_five/style1.css" rel="stylesheet" type="text/css">
<link rel="icon" href="/assign_five/Bokehlicia-Captiva-File-manager.ico">
<!--script src="/jquery-1.11.3.js" type="text/javascript"></script-->
<title>Assignment 5 Home Page</title>
</head>
    <body>
        <div id="main_content_area">
            <div id="main_title_navbar">
                <div id="title_space">Internet Programming: Assignment 5</div>
                <div id="link_one"><a href="/assign_five/a5_home_page.html">Home Page</a></div>
                <div id="link_two"><a href="/cgi-bin/area_selection.py">Select an Area</a></div>
                <div id="link_two"><a href="/assign_five/a5_error_testing_page.html">Error Testing</a></div>
                <div id="symbol_space">
                   <img src="/assign_five/5Cubes2.png" height="150px" width="150px"/>
                </div>
            </div>""")

a = get_all_areas()
category = ""
num = 1

#table space for database entries:
print("""<div id="page_body2">Table of Areas</br><table class=\"grid\"><th class=\"grid\">ID</th><th class=\"grid\">Name</th>
<th class=\"grid\">Number of Locations</th><th class=\"grid\">Average Value</th>
<th class=\"grid\">Categories</th>""")

for x in a:

    b = number_of_locations_by_area(num)
    c = get_average_measurements_for_area(num)
    d = get_categories_for_area(num)
    spec1 = (27-(len(x['name'])+2))

    if not d: #if categories returns none
        category = ""
    else: #if categories returns a list
        for C in d:
            category += C['name']+" "
    if not c:
        total = "{0:} {1:} {2:>"+str(spec1)+"} {3:>19} {4:>7}"
        cc = "----------"
        # print(total.format(num, x['name'], b, cc, category))r
        print("<tr><td>" + str(num) + "</td><td>" + x['name'] + "</td><td>" + str(b) + "</td><td>" + str(cc) + "</td><td>" + category + "</td></tr>")
    else:
        # nString = str(num)
        ave_val = str(c)
        # print(total.format(num, x['name'], b, c, category))
        print("<tr><td>" + str(num) + "</td><td>" + x['name'] + "</td><td>" + str(b) + "</td><td>" + "{:.2f}".format(c) + "</td><td>" + category + "</td></tr>")
    num = num + 1

    category = "" #must be redeclared upon each pass of the loop

print("</table></div></div></body></html>")

