from flask import Flask
from blueprints.View import main_blueprint
from database import db
from flask_migrate import Migrate

import setting

app = Flask(__name__)

# Database
# step 1 get parameter of sqlite database
app.config.from_object(setting)
# step 2 Connecting the database to the app.py
db.init_app(app)
#
migrate = Migrate(app, db)

# blueprints
app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run()
