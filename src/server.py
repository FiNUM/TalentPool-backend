from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)
import models as models
import datetime


@app.route('/users', methods=['POST'])
def create_checkout():
    # bot = (request.form['username'],
    #        request.form['password'])
    graduation = models.Graduation(graduation=request.form['graduation'])

    language = models.Languages(language=request.form['language'], ability=request.form['bla'])
    db.session.add(language)

    studies = models.Studies(studies=request.form['bla'], periodFrom=request.form['bla'], periodTo=request.form['bla'])

    itSkills = models.ItSkills(itSkills=request.form['bla'], knowledge=request.form['bla'])

    furtherEducation = models.FurtherEducation(education=request.form['bla'])

    profExp = models.ProfessionalExperience(company=request.form['bla'], periodFrom=request.form['bla'],
                                            periodTo=request.form['bla'])

    applications = models.Applications(company=request.form['bla'])

    lead_positions = models.LeadingPositions(previousLeadingPosition=request.form['bla'],
                                             nrOfPplResponsible=request.form['bla'])

    models.TempTP(name=request.form['name'], forename=request.form['forename'], birthday=request.form['birthday'],
                  nationality=request.form['nationality'], email=request.form['email'],
                  telephoneNumber=request.form['telnr'], address=request.form['nationality'],
                  desiredPosition=request.form['desiredPosition'], startingDate=request.form['startingDate'],
                  graduation=graduation.id, apprenticeship=request.form['nationality'],
                  timestamp=datetime.datetime.now(),
                  languageTable=language.id, studiesTable=studies.id,
                  itSkillsTable=itSkills.id, furtherEducationTable=furtherEducation.id,
                  professionalExpTable=profExp.id, applicationsTable=applications.id,
                  leadershipTable=lead_positions.id, careerGoals=request.form['careerGoals'], )

    db.session.commit()

    return "DONE"


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
