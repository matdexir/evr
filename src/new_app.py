from typing import Type
from rich.console import RenderableType
from textual.app import App
from textual.driver import Driver
from textual.reactive import Reactive
from textual.views import GridView
from textual_inputs.text_input import TextInput
from textual.widgets import Header, Footer, Button, Placeholder


class TodoGrid(GridView):
    async def on_mount(self) -> None:
        self.grid.set_gap(1, 1)
        self.grid.add_column("all-todos")
        self.grid.add_row("todo-item", repeat=5)
        placeholders = (Placeholder() for _ in range(5))
        self.grid.place(*placeholders)


class InputGrid(GridView):
    async def on_mount(self) -> None:
        self.new_todo = TextInput(
            name="todo", placeholder="Please enter a new todo", title="New Todo"
        )
        # self.submit_label = Button(label="submit", name="submit_label", style="bold red on white")
        self.anything = TodoGrid()
        # self.grid.set_align("center", "center")
        self.grid.set_gap(1, 1)
        self.grid.add_column("column", repeat=2)
        self.grid.add_row("row")
        self.log("InputGrid is mounted")
        self.grid.add_widget(self.anything)
        self.grid.add_widget(self.new_todo)


class MyApp(App):
    def __init__(
        self,
        screen: bool = True,
        driver_class: Type[Driver] | None = None,
        log: str = "",
        log_verbosity: int = 1,
        title: str = "Textual Application",
    ) -> None:
        super().__init__(screen, driver_class, log, log_verbosity, title)

    async def on_load(self) -> None:
        await self.bind("q", "quit", "Quit")
        await self.bind("enter", "submit", "Submit")
        await self.bind("escape", "reset_focus", show=False)

    async def on_mount(self) -> None:
        self.input_grid = InputGrid()

        self.header = Header()
        self.footer = Footer()

        await self.view.dock(self.header, edge="top")
        await self.view.dock(self.footer, edge="bottom")
        await self.view.dock(self.input_grid, edge="left")

    async def action_reset_focus(self) -> None:
        await self.header.focus()

    async def action_submit(self) -> None:
        self.log("List submitted")
        self.input_grid.new_todo.value = ""


if __name__ == "__main__":
    MyApp.run(title="EVR", log="textual.log")
