from server import db


class TempTP(db.Model):
    __tablename__ = 'temptp'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    forename = db.Column(db.String(80), unique=True, nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    nationality = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80))
    telephoneNumber = db.Column(db.Integer)
    address = db.Column(db.String(200))
    desiredPosition = db.Column(db.String(100))
    # earliest starting date
    startingDate = db.Column(db.Date)
    graduation = db.Column(db.String(100), nullable=False)
    apprenticeship = db.Column(db.String(100))
    timestamp = db.Column(db.TIMESTAMP, nullable=False)
    languageTable = db.relationship('languages', backref='temptp', lazy=True)
    studiesTable = db.relationship('studies', backref='temptp', lazy=True)
    itSkillsTable = db.relationship('it_skills', backref='temptp', lazy=True)
    furtherEducationTable = db.relationship('further_education', backref='temptp', lazy=True)
    professionalExpTable = db.relationship('professional_experience', backref='temptp', lazy=True)
    applicationsTable = db.relationship('applications', backref='temptp', lazy=True)
    leadershipTable = db.relationship('leading_positions', backref='temptp', lazy=True)
    careerGoals = db.Column(db.Text)
    salaryExpectations = db.Column(db.Integer)
    salaryFactors = db.Column(db.Text)
    regionallyAvailable = db.Column(db.Boolean)
    nationalAvailable = db.Column(db.Boolean)

    def __repr__(self):
        return '<TempTP %r>' % self.name


class LeadingPositions(db.Model):
    __tablename__ = 'leading_positions'
    id = db.Column(db.Integer, primary_key=True)
    previousLeadingPosition = db.Column(db.String(100))
    nrOfPplResponsible = db.Column(db.Integer, nullable=False)
    temptp_id = db.Column(db.Integer, db.ForeignKey('temptp.id'), nullable=False)


class Applications(db.Model):
    __tablename__ = 'applications'
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    temptp_id = db.Column(db.Integer, db.ForeignKey('temptp.id'), nullable=False)


class ProfessionalExperience(db.Model):  # what if you have no Experience?
    __tablename__ = 'professional_experience'
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100))
    position = db.Column(db.String(100))
    periodFrom = db.Column(db.Date, nullable=False)
    periodTo = db.Column(db.Date, nullable=False)
    temptp_id = db.Column(db.Integer, db.ForeignKey('temptp.id'), nullable=False)


class FurtherEducation(db.Model):  # what if you have no further education?
    __tablename__ = 'further_education'
    id = db.Column(db.Integer, primary_key=True)
    education = db.Column(db.String(100))
    temptp_id = db.Column(db.Integer, db.ForeignKey('temptp.id'), nullable=False)


class Studies(db.Model):  # Studium
    __tablename__ = 'studies'
    id = db.Column(db.Integer, primary_key=True)
    studies = db.Column(db.String(100))
    periodFrom = db.Column(db.Date, nullable=False)
    periodTo = db.Column(db.Date, nullable=False)
    temptp_id = db.Column(db.Integer, db.ForeignKey('temptp.id'), nullable=False)


class ItSkills(db.Model):
    __tablename__ = 'it_skills'
    id = db.Column(db.Integer, primary_key=True)
    itSkills = db.Column(db.String(100))
    knowledge = db.Column(db.Integer)  # how good is your skill
    temptp_id = db.Column(db.Integer, db.ForeignKey('temptp.id'), nullable=False)


class Languages(db.Model):
    __tablename__ = 'languages'
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(80), nullable=False)
    # knowledge how good you speak it:
    ability = db.Column(db.Integer, nullable=False)
    temptp_id = db.Column(db.Integer, db.ForeignKey('temptp.id'), nullable=False)


def list_tables():
    return [TempTP, Languages, ItSkills, Studies, FurtherEducation, ProfessionalExperience, Applications,
            LeadingPositions]