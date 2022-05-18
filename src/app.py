import rich.box

from typing import TYPE_CHECKING

from rich.panel import Panel
from rich.style import Style
from rich.table import Table 
from rich.text import Text

from textual.app import App
from textual.reactive import Reactive
from textual.widgets import Footer, Header, Static 

from textual_inputs import TextInput, IntegerInput

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
    def __init__(self):
        raise NotImplementedError
    async def on_load(self) -> None:
        raise NotImplementedError
    async def on_event(self, event: events.Event) -> None:
        #  return await super().on_event(event)
        raise NotImplementedError
    async def on_message(self, message: Message) -> None:
        #  return await super().on_message(message)
        raise NotImplementedError
