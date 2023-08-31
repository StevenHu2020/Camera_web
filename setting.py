# no session
# SECRET_KEY = "asdfasdfjasdfjasd;lf"

# Linking database connection information
import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(basedir, "Camera.sqlite")

# Startup Related Parameters (abandoned)
DEBUG = True
WEBSITE_PORT = '7000'
