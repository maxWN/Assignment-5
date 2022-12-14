# Assignment-5 Northwest Georgia Geography Site

**Project Status:**

This project has not been actively maintained for a considerable amount of time. It is in an archived state, so please refrain from making any pull requests or using in any capacity beyond its original intended purpose.

- Software used:
- Ubuntu 14.04 
- Apache 2.4.7
- Python 3.4.0

**Summary:**

This application uses the measurements example database as a subject. It uses the modules db_access and db_utility functions to access data regarding geographical and infastructure features of local towns in Georgia. There are four additional Python scripts that generate new forms (using db_access.py and db_utility.py functions) upon receiving user data. 

**Error Handling:**

Each script handles errors in the submitted data:

- No id submitted
- Submitted id is not an integer
- Submitted id is not the id of an actual entity in the database

When location_table.py detects an error, it will redisplay the area_selection.py page with an appropriate message. When measurement_table.py detectc an error, it will display a generic error page with messages. There is an HTML page (reachable from the home page) that contains six froms with three error possibilities times two scripts (location_table.py and measurement_table.py). 

**Purpose**

The overall purpose for the code contained within this repository is for demonstration purposes. It is not intended for open source development, as it is only intended to demonstrate knowledge of web programming in the Python programming language.
