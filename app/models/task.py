from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)
    completed_at = db.Column(db.DateTime, nullable = True)

    def to_dict(self):
        return {
            "id": self.task_id,
            "title": self.title,
            "description": self.description,
            "is_complete": True if self.completed_at else False
        }

    def one_task_in_dict(self):
        result = {}
        result["task"] = self.to_dict()
        return result
    
    def one_saved_task(self, data_dict):
        self.title = data_dict["title"]
        self.description = data_dict["description"]

