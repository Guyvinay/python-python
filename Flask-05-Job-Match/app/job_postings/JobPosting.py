class JobPosting : 
    def __init__(self, title, status, start_date, end_date, hiring_manager_id):
        self.title = title
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        self.hiring_manager_id = hiring_manager_id

    def to_dict(self):
        return {
            'title': self.title,
            'status': self.status,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'hiring_manager_id': self.hiring_manager_id
        }    