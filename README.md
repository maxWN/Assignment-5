# Assignment-5

**Summary:**

This code was submitted as the solution for [Assignment 5](https://ksuweb.kennesaw.edu/~bsetzer/old/4720fa15/nanoc/output/assignments/5/) for KSU course *Internet Programming* in the fall of 2015. This web application uses the measurements example database as a subject. It uses the modules db_access and db_utility functions to access data regarding geographical and infastructure features of local towns in Georgia. There are four additional Python scripts that generate new forms (using db_access.py and db_utility.py functions) upon receiving user data. 

**Application Dependencies:**

This web application requires the following dependencies to properly function:

- Ubuntu 14.04 (or greater)
- Apache Server 2.4.7 (or greater)
- Python 3.4.0

**Error Handling:**

Each script handles errors in the submitted data:

- No id submitted
- Submitted id is not an integer
- Submitted id is not the id of an actual entity in the database

When location_table.py detects an error, it will redisplay the area_selection.py page with an appropriate message. When measurement_table.py detects an error, it will display a generic error page with messages. There is an HTML page (reachable from the home page) that contains six froms with three error possibilities times two scripts (location_table.py and measurement_table.py). 
