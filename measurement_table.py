#!/usr/bin/python3

__author__ = 'Max W. Nakel'

import cgi
import cgitb
from db_access import get_locations_for_area, get_categories_for_area, get_all_areas, get_measurements_for_location, get_area_by_id, get_location_by_id
from db_utility import number_of_locations_by_area, get_average_measurements_for_area

cgitb.enable()

print("Content-Type:text/html; charset=UTF-8")
# print("Content-Type: html/text; charset: UTF-8")
print()

collect = cgi.FieldStorage()
user_val = collect.getfirst("location_id")

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
                <div id="link_one"><a href="/assign_five/a5_home_page.html">Home Page</a></div>
                <div id="link_two"><a href="/cgi-bin/area_table.py">Display all Areas</a></div>
                <div id="link_two"><a href="/assign_five/a5_error_testing_page.html">Error Testing</a></div>
                <div id="symbol_space">
                   <img src="/assign_five/5Cubes2.png" height="150px" width="150px"/>
                </div>
            </div>""")

bool = True
if user_val != None:
    for abc in user_val:
        if abc.isdigit() == False:
            bool = False

if user_val != None and bool:

    a = get_measurements_for_location(user_val)
    b = get_location_by_id(user_val)
    c = get_all_areas()
    if a == None or b == None or c == None:
        print("<div id=\"error_page\"><strong>ERROR: User entered an ID which was not found!</strong></div>")
    else:
        formatted = 0
        iterate = 0
        for y in b:
            area = y['location_area']
            print("<div id=\"page_body2\"><U>Measurements for " + y['name'] + "</U></br></br><table class=\"grid\"><th class=\"grid\">ID</th><th class=\"grid\">Value</th>")
        for x in a:
            formatted += x['value']
            iterate = iterate + 1
            print("<tr><td>" + user_val + "</td><td>" + "{:.2f}".format(x['value']) + "</td></tr>")

        ave_location_val = formatted/iterate
        print("</table></br><U>Average Measurement of Location:</U> " + "{:.2f}".format(ave_location_val) + "</U></div></body></html>")

    # str(x['measurement_location'])

elif user_val == None:
    print("<div id=\"error_page\"><strong>ERROR: User did not make a valid selection!</strong></div>")

elif bool == False:
    print("<div id=\"error_page\"><strong>ERROR: User selected data that was not of integer data type!</strong></div>")


