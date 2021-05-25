"""Runs the multicblaster web service

Author: Matthias van den Belt
"""

# own project imports
from multicblaster import app

### main code
if __name__ == "__main__":
    print(app.config)
    app.run(host=app.config["HOST"], port=app.config["PORT"])

    # lets other computers within the same network access the web pages
    # by typing the following address in a web browser:
    #       "<ip_of_pc_where_this_module_is_ran_from>:5001"
