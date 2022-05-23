#  import os
#  import sys

import rich.box

#  from rich.text import Text
from rich.console import RenderableType
from rich.panel import Panel
#  from rich.text import Text
#  from textual.geometry import Size

#  from rich.syntax import Syntax

#  from rich.style import Style
#  from rich.traceback import Traceback
from textual import events
from textual.app import App
#  from textual.message import Message
from textual.reactive import Reactive
from textual.widgets import DirectoryTree, ScrollView, Static, Footer
from textual_inputs import IntegerInput, TextInput

from definitions.todo_item import todoItem
from layout.header import CustomHeader



class MainApp(App):
    """
    This is the main class definition for my app. There you can find all the key binds and other layout configs
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.todo_items = []
        self.path = ".."

    async def on_load(self, event: events.Load) -> None:
        await self.bind("q", "quit", "Quit")
        await self.bind("enter", "submit", "Submit")
        await self.bind("escape", "reset_focus", show=False)

    async def on_mount(self, event: events.Mount) -> None:
        self.insert_todo = TextInput(
            name="todos",
            placeholder="what next todo",
            title="todos",
        )
        self.insert_todo.on_change_handler_name = "handle_insert_todo_change"

        self.age = IntegerInput(
            name="age",
            placeholder="enter your age...",
            title="Age",
        )
        self.age.on_change_handler_name = "handle_age_change"

        self.header = CustomHeader()
        #  self.directory = DirectoryTree(self.path, "Code")
        self.footer = Footer()

        self.output = ScrollView(
            Panel("", title="Report", border_style="blue", box=rich.box.SQUARE)
        )

        #  Header and footer
        await self.view.dock(self.header, edge="top")
        await self.view.dock(self.footer, edge="bottom")
        await self.view.dock(self.output, edge="left", size=50)

        await self.view.dock(self.insert_todo, edge="right", size=50)

    async def action_submit(self) -> None:
        self.todo_items.append(todoItem(self.insert_todo.value))
        self.insert_todo.value = ""
        #  formatted = "\n".join([str(item.content) for item in self.todo_items])
        items = tuple(self.todo_items)
        await self.view.dock(*items, size=30)
        #  self.log(f"The todos are: {formatted}")

    async def action_reset_focus(self) -> None:
        await self.header.focus()

    #  async def handle_insert_todo_change(self, message: Message) -> None:
        #  self.log(f"The value of self.insert_todo is: {message.sender.value}")

    #  async def handle_age_change(self, message: Message) -> None:
        #  self.log(f"The value of self.age is: {message.sender.value}")


if __name__ == "__main__":
    MainApp.run(title="EVR", log="textual.log")
