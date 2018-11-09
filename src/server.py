from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)
import models as models

@app.route('/users', methods=['POST'])
def create_checkout():
    bot = (request.form['username'],
              request.form['password'])
    for f in request.form:
        if not (f == 'username' or f == 'password') and request.form[f] == 'on':
            try:
                app.logger.info('Starting: %s' % f)
            except Exception as e:
                app.logger.warning(e)

    return "DONE"

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
