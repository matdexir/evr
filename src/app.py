#  import rich.box
import os
import sys

#  from rich.panel import Panel
#  from rich.style import Style
#  from rich.table import Table
#  from rich.text import Text
from rich.console import RenderableType
from rich.syntax import Syntax
from rich.traceback import Traceback

from textual import events
from textual.app import App
from textual.reactive import Reactive
from textual.widgets import Footer, Header, FileClick, ScrollView, DirectoryTree   

#  from textual_inputs import TextInput, IntegerInput


class CustomHeader(Header):
    '''
    Customization for the header side of the TUI
    '''
    def __init__(self):
        raise NotImplementedError
    def render(self):
        raise NotImplementedError
    async def on_click(self):
        raise NotImplementedError

class CustomFooter(Footer):
    '''
    Customization for the footer side of the TUI
    '''
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
        self.path = ".."
        
    async def on_load(self, event: events.Load) -> None:
        await self.bind("q", "quit", "Quit")
        await self.bind("enter", "submit", "Submit")
        await self.bind("escape", "reset_focus", show=False)

    async def on_mount(self, event: events.Mount) -> None:

        self.body = ScrollView() 
        self.directory = DirectoryTree(self.path, "Code") 

        #  Header and footer
        await self.view.dock(Header(), edge="top")
        await self.view.dock(Footer(), edge="bottom")
        
        # Basic body structure
        await self.view.dock(
            ScrollView(self.directory), edge="left", size=25, name="sidebar"   
        )
        await self.view.dock(self.body, edge="top")

    async def handle_file_click(self, message: FileClick) -> None:
        """A message sent by the directory tree when a file is clicked."""

        syntax: RenderableType

        try:
            # Construct a Syntax object for the path in the message
            syntax = Syntax.from_path(
                message.path,
                line_numbers=True,
                word_wrap=True,
                indent_guides=True,
                theme="dracula",
                background_color=None
            )
        except Exception:
            # Possibly a binary file
            # For demonstration purposes we will show the traceback
            syntax = Traceback(theme="monokai", width=None, show_locals=True)
        #  self.sub_title = os.path.basename(message.path)
        await self.body.update(syntax)

if __name__ == '__main__':
    MainApp.run(title="EVR" ,log="textual.log")
