#  import rich.box

from typing import TYPE_CHECKING

#  from rich.panel import Panel
#  from rich.style import Style
#  from rich.table import Table
#  from rich.text import Text

from textual import events
from textual.app import App
#  from textual.reactive import Reactive
from textual.widgets import Footer, Header,   

#  from textual_inputs import TextInput, IntegerInput

if TYPE_CHECKING:
   from textual.message import Message


class CustomHeader(Header):
    def __init__(self):
        raise NotImplementedError
    def render(self):
        raise NotImplementedError
    async def on_click(self):
        raise NotImplementedError

class CustomFooter(Footer):
    def __init__(self):
        raise NotImplementedError
    def render(self):
        raise NotImplementedError
    async def on_click(self):
        raise NotImplementedError

class MainApp(App):
    '''
        This is the main class definition for my app. There you can find all the key binds and other layout configs
    '''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.todo_items = []
        
    async def on_load(self, event: events.Load) -> None:
        await self.bind("q", "quit", "Quit")
        await self.bind("enter", "submit", "Submit")
        await self.bind("escape", "reset_focus", show=False)

    async def on_mount(self, event: events.Mount) -> None:
        await self.view.dock(Header(), edge="top")
        await self.view.dock(Footer(), edge="bottom")

if __name__ == '__main__':
    MainApp.run(title="EVR" ,log="textual.log")
