import uuid
from rich.panel import Panel
from rich.text import Text
from textual.app import log
from textual.geometry import Size
from textual.reactive import Reactive
from textual.widget import Widget


class todoItem(Widget):
    """
    Definition of a todo item
    """
    mouse_over = Reactive(False)
    def __init__(self, content):
        super().__init__()
        self.content = Text(content)
        self.ID = uuid.uuid4() 
    def on_click(self):
        log(f"Click {self.content} with ID {self.ID}")
    def on_enter(self):
        self.mouse_over = True
    def on_leave(self):
        self.mouse_over = False
    def render(self) -> Panel:
        return Panel(self.content, style=("on red" if self.mouse_over else ""))
        
    def __repr__(self):
        return f"Content: {self.content}\n ID:{self.ID}\n"
