from textual.widgets import Header

from rich.table import Table
from rich.style import Style

class CustomHeader(Header):
    """
    Customization for the header side of the TUI
    """

    def __init__(self):
        super().__init__()
        self.tall = False
        self.style = Style(color="black", bgcolor="blue")

    def render(self) -> Table:
        header_table = Table.grid(padding=(0, 1), expand=True)
        header_table.add_column("Title", justify="center", ratio=1)
        header_table.add_column("Clock", justify="right", width=10)
        header_table.add_row(self.full_title, self.get_clock())
        return header_table
