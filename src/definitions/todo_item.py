import uuid
from rich.text import Text

class todoItem:
    """
    Definition of a todo item
    """
    def __init__(self, content):
        self.content = Text(content)
        self.ID = uuid.uuid4() 
    def on_click(self):
        raise NotImplemented
    def __repr__(self):
        return f"Content: {self.content}\n ID:{self.ID}\n"
