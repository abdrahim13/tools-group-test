
from dataclasses import dataclass
import datetime
from app import db


"""
Todo model
"""


@dataclass
class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120), nullable=False)
    done = db.Column(db.Boolean, default=False)
    important = db.Column(db.Boolean, default=False)
    deadline_date = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, text, done=False, important=False):
        self.text = text
        self.done = done
        self.important = important

    def save(self):
        """
        save in the database
        """

        db.session.add(self)
        db.session.commit()
        return True

    def delete(self):
        """
        delete from database
        """

        db.session.delete(self)
        db.session.commit()
        return True

    def update(self, data):
        """
        update todo
        """
        # 
        if "deadlineDate" in data:
            # fix date format from frontend iSO 8601 to python date
            deadline_date = data.pop("deadlineDate")
            data["deadline_date"] = datetime.datetime.strptime(
                deadline_date, "%Y-%m-%dT%H:%M:%S.%fZ")

        # Update the Todo instance directly
        for key, value in data.items():
            setattr(self, key, value)
            
        db.session.commit()
        
        return True

    def __repr__(self):
        return "Todo <text={} done={} important={} id={}>".format(self.text, self.done, self.important, self.id)

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'done': self.done,
            'important': self.important,
            'deadlineDate': self.deadline_date.strftime('%Y-%m-%dT%H:%M:%SZ')
        }

    @staticmethod
    def list_to_json(todos):
        return [todo.to_dict() for todo in todos]
