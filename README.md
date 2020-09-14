# Wedding List Technical Challenge

This program was created by implementing the least amount of libraries (SQL alchemy, react js, jinja templating etc...) possible in a rudimentary way without hindering development.

Project finished in 1-2 days.

Raw AJAX calls were used to send data from front to back end and vice versa.

All code was hand-written with no boiler-plates used.

The two libraries installed (with their own dependencies) are:
 * Flask
 * psycopg2 database adapter to connect to the PostgreSQL database engine
 
## Setup
    1) pip install -r requirements.txt
    2) make sure you have PostgreSQL installed on your computer with the default db (postagre) and default settings for it
    3) run "models.py" to create the new database and tables required
    4) run main.py and open the site up locally
    5) That's it, no need to complicate things with a build script / CI for this... (in my opinion of course :) )

## Final Thoughts
This is a simple application that runs the program asked with all the "meaty" bits.

 For simplicity's sake, some things were left out from the development of this project, due to the small code base and unnecessary complications such as:
 * A docker image could have been created to containerize this whole program 
 * Build script to automatically set all dependencies and requirements needed to run this
 * Unit tests (The skeleton for these tests was created, but the actual tests were not created)
 * API documentation
 * More complex logging for debugging, errors etc (only a few logs are kept and the rest are done with prints)
 * Project layout could have been improved greatly (as this is a small project, it does not hinder it much at all)
 * Add user authentication
 * Add a few layers and alter the way data is passed to prevent SQL injection (outside the scope of this project)
 * Add pagination to the products and list pages
 * Add HTTP status codes to each endpoint
 * Add a payment/checkout page
