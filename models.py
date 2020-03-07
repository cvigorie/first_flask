from app import db

class Result(db.Model):
    __table_args__ = {'schema' : 'ced'}
    __tablename__ = 'linregresults'

    id = db.Column(db.Integer, primary_key = True)
    experience = db.Column(db.Integer)
    predicted_salary = db.Column(db.Integer)

    def __init__(self, experience, predicted_salary):
        self.experience = experience
        self.predicted_salary = predicted_salary

    def __repr__(self):
        return '<id {}>'.format(self.id)