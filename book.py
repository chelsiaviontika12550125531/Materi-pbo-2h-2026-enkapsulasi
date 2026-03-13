from datetime import datetime

class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.last_updated = datetime.now()
    
    def get_id(self):
        return self.id
    
    def get_title(self):
        return self.title
    def set_title(self, new_title):
        self.title = new_title
    
    def get_author(self):
        return self.author
    def set_author(self, new_author):
        self.author = new_author
