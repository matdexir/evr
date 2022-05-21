#  import os
#  import sys

import rich.box

#  from rich.text import Text
from rich.console import RenderableType
from rich.panel import Panel
from rich.style import Style
from rich.text import Text
#  from rich.syntax import Syntax

#  from rich.style import Style
from rich.table import Table
from rich.traceback import Traceback
from textual import events
from textual.app import App
from textual.message import Message
from textual.reactive import Reactive
from textual.widgets import DirectoryTree, Footer, Header,ScrollView, Static
from textual_inputs import IntegerInput, TextInput

from definitions.todo_item import todoItem


class CustomHeader(Header):
    """
    Customization for the header side of the TUI
    """

    def __init__(self):
        super().__init__()
        self.tall = False
        self.style = "dark on white"
        self.style = Style(color="white", bgcolor="blue")

    def render(self) -> Table:
        header_table = Table.grid(padding=(0, 1), expand=True)
        header_table.add_column("Title", justify="center", ratio=1)
        header_table.add_column("Clock", justify="right", width=10)
        header_table.add_row(self.full_title, self.get_clock())
        return header_table

class CustomFooter(Footer):
    """
    Customization for the footer side of the TUI
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def render(self) -> None:
        raise NotImplementedError

    async def on_click(self) -> None:
        raise NotImplementedError


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
        self.new_todo = TextInput(
            name="todos",
            placeholder="what next todo",
            title="todos",
        )
        self.new_todo.on_change_handler_name = "handle_new_todo_change"

        self.age = IntegerInput(
            name="age",
            placeholder="enter your age...",
            title="Age",
        )
        self.age.on_change_handler_name = "handle_age_change"

        self.header = CustomHeader()
        self.directory = DirectoryTree(self.path, "Code")
        self.footer = Footer()


        self.output = ScrollView(
            Panel(
                "", title="Report", border_style="blue", box=rich.box.SQUARE, height=15
            )
        )

        #  Header and footer
        await self.view.dock(self.header, edge="top")
        await self.view.dock(self.footer, edge="bottom")
        await self.view.dock(self.output, edge="left", size=40)

        # Basic body structure
        #  await self.view.dock(
        #  ScrollView(self.directory), edge="left", size=30, name="sidebar"
        #  )
        await self.view.dock(self.new_todo, edge="right", size=30)

    async def action_submit(self) -> None:
        self.todo_items.append(todoItem(self.new_todo.value))
        self.new_todo.value = ""
        formatted = "\n".join([str(item.content) for item in self.todo_items])
        await self.output.update(Panel(formatted, title="Todos", height=15))
        self.log(f"The todos are: {formatted}")
        #  self.log(f"{self.todo_items}")

    async def action_reset_focus(self) -> None:
        await self.header.focus()

    async def handle_new_todo_change(self, message: Message) -> None:
        self.log(f"The value of self.new_todo is: {message.sender.value}")

    async def handle_age_change(self, message: Message) -> None:
        self.log(f"The value of self.age is: {message.sender.value}")


if __name__ == "__main__":
    MainApp.run(title="EVR", log="textual.log")
