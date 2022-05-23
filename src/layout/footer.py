from textual.widgets import Footer

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

