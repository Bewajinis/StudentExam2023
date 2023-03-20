from ..utilis import db
from enum import Enum 
from datetime import datetime

class Grades(Enum):
    A = 4.5
    B = 4.0
    C = 3.5
    D = 3.0
    E = 2.0
    F = 1.5



class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    teacher = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.Enum(Grades), default=Grades.F)
    date_created = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    student = db.Column(db.Integer(), db.ForeignKey('students.id'))

    def __repr__(self):
        return f"<Course {self.name}>" 
    
    