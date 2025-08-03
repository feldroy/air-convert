"""Console script for air_convert."""

from pathlib import Path

import typer
from rich.console import Console

from .air_convert import html_to_airtags

app = typer.Typer()
console = Console()


@app.command()
def main(target: Path, output: Path | None = None):
    """Convert HTML to Air Tags. If output is None result is sent to STDOUT.

    Try it with "air_convert path/to/my.html > mypage.py"
    """
    html = target.read_text()
    result = html_to_airtags(html)
    if output is None:
        console.print(result, soft_wrap=True)
    else:
        output.write_text(result)
        console.print(f"Air Tags saved to {output}")


if __name__ == "__main__":
    app()
