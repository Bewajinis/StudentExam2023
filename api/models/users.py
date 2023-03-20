from ..utilis import db 


class User(db.Model):
      __abstract__ = True

      first_name = db.Column(db.String(45), nullable=False)
      last_name = db.Column(db.String(45), nullable=False)
      username = db.Column(db.String(45), nullable=False,  unique=True)
      email = db.Column(db.String(58), nullable=False, unique=True)
      password_hash = db.Column(db.Text(), nullable=False)
      gpa = db.Column(db.Float, nullable=False, default=0-0.)
      admin = db.Column(db.Boolean(), default=False)
      is_active = db.Column(db.Boolean(), nullable=False, default=False)

    


class Student(User):
    __tablename__ = 'students'
    id = db.Column(db.Integer(), primary_key=True)
    courses = db.relationship('Course', backref='students', lazy=True)
    gpa = db.Column(db.Float, default=0.0)


    def __repr__(self):
        return f"<Student {self.username}>" 
    

class Admin(User):
     __tablename__= 'admins'
     id = db.Column(db.Integer(), primary_key=True)

     def __repr__(self):
        return f"<Admin {self.username}>"