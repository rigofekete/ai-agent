from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.widgets import LoadingIndicator, RichLog, TextArea
from textual import work
import asyncio


class AgentTui(App):
    FONT = "JetBrainsMono NFM"

    BINDINGS = [Binding("ctrl+q", "quit", "Quit")]

    CSS = """
    Screen {
        align: center middle;
        background: #060b1e;
    }

    #output-log {
        width: 80;
        height: 1fr;
        max-height: 10;
        background: #060b1e;
        color: #ffcead;
        padding: 1 2;
        border: none;
        scrollbar-size: 0 0;
    }

    #prompt-wrap {
        width: 80;
        height: auto;
        padding: 0 0;
        border-top: heavy #c89dc1;
        border-bottom: heavy #c89dc1;
        border-subtitle-color: #ffcead;
        border-subtitle-style: italic;
    }

    #prompt {
        background: #12215c;
        color: #ffcead;
        padding: 1 2;
        border: none;
        height: 5;
    }

    #prompt > .text-area--cursor-line {
        background: #12215c;
    }

    #loader {
        display: none;
        width: 80;
        height: 1;
        color: cyan;
    }

    #loader.running {
        display: block;
    }
    """

    def compose(self) -> ComposeResult:
        yield RichLog(id="output-log", highlight=True, markup=True, wrap=True)
        yield Vertical(
            TextArea(placeholder="Type your prompt here...", id="prompt"),
            id="prompt-wrap",
        )
        yield LoadingIndicator(id="loader")

    def on_mount(self) -> None:
        wrap = self.query_one("#prompt-wrap", Vertical)
        wrap.border_subtitle = " ctrl+q to quit "

        self.query_one("#prompt", TextArea).focus()

    def on_text_area_changed(self, event: TextArea.Changed) -> None:
        if event.text_area.id != "prompt":
            return
        if event.text_area.text.endswith("\n"):
            text = event.text_area.text.rstrip("\n")
            if text:
                event.text_area.load_text("")
                self.run_prompt(text)

    @work
    async def run_prompt(self, prompt_text: str) -> None:
        log = self.query_one("#output-log", RichLog)
        loader = self.query_one("#loader", LoadingIndicator)

        log.write(f"[bold cyan]> {prompt_text}[/]")
        loader.add_class("running")

        try:
            process = await asyncio.create_subprocess_exec(
                "python",
                "-u",
                "main.py",
                prompt_text,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.STDOUT,
            )

            assert process.stdout is not None
            async for raw_line in process.stdout:
                line = raw_line.decode(errors="replace").rstrip("\n")
                if line:
                    log.write(line)

            await process.wait()
            log.write("")
        except Exception as exc:
            log.write(f"[red]error:[/] {exc}")
        finally:
            loader.remove_class("running")


if __name__ == "__main__":
    AgentTui().run()
