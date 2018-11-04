from app import db


class TempTP(db.Model):
    __tablename__ = 'temptp'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    settings = db.Column(db.Text(), nullable=False)
    timestamp = db.Column(db.TIMESTAMP, nullable=False)
    paid = db.Column(db.Boolean, default=False)
    started = db.Column(db.Boolean, default=True)
    languagetable = db.relationship('Languages', backref='temptp', lazy=True)

    def __repr__(self):
        return '<TempTP %r>' % self.username


class Languages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(80), nullable=False)
    #Knowledge how good you speak it:

    temptp_id = db.Column(db.Integer, db.ForeignKey('temptp.id'), nullable=False)


def list():
    return [TempTP, Languages]
