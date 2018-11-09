from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)
import models as models


@app.route('/users', methods=['POST'])
def create_checkout():
    # bot = (request.form['username'],
    #        request.form['password'])

    language = models.Languages(language=request.form['language'], ability=request.form['bla'])
    db.session.add(language)

    models.Studies(studies=request.form['bla'], periodFrom=request.form['bla'], periodTo=request.form['bla'])

    models.ItSkills(itSkills=request.form['bla'], knowledge=request.form['bla'])

    models.FurtherEducation(education=request.form['bla'])

    models.ProfessionalExperience(company=request.form['bla'], periodFrom=request.form['bla'], periodTo=request.form['bla'])

    models.Applications(company=request.form['bla'])

    models.LeadingPositions(previousLeadingPosition=request.form['bla'], nrOfPplResponsible=request.form['bla'])

    models.TempTP(forename=request.form['forename'], languageTable=language.id)

    db.session.commit()

    return "DONE"


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
