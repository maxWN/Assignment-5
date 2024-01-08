#!/usr/bin/python3

__author__ = 'Max W. Nakel'

import cgi
import cgitb
from db_access import get_locations_for_area, get_categories_for_area, get_all_areas, get_measurements_for_location
from db_utility import number_of_locations_by_area, get_average_measurements_for_area

cgitb.enable()

print("Content-Type:text/html; charset=UTF-8")
# print("Content-Type: html/text; charset: UTF-8")
print()

print("""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="/assign_five/style1.css" rel="stylesheet" type="text/css">
<link rel="icon" href="/assign_five/Bokehlicia-Captiva-File-manager.ico">
<script src="/jquery-1.11.3.js" type="text/javascript"></script>
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
a = get_all_areas()
print("<div id=\"page_body2\">Select an Area</br><form method=\"get\" action=\"/cgi-bin/location_table.py\"><select name=\"area_id\" size=\"5\">")
for x in a:

    print("<option value=\"" + str(x['area_id']) + "\">" + x['name'] + "</option>")

print("</select></br><input id=\"sButton\" type=\"submit\" value=\"Submit\"></form></div></div></body></html>")

