# Assignment-5 Northwest Georgia Geography Site

Author: Max W. Nakel

Created: 10/24/2015

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
