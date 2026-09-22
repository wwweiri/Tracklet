import typer

app = typer.Typer(
    name="tracklet",
    help="Lightweight ML experiment tracker",
    no_args_is_help=True,
)

@app.callback()
def main():
    """Lightweight local ML experiment tracker."""
    pass


@app.command()
def hello():
    """Simple test command."""
    print("Tracklet works!")


if __name__ == "__main__":
    app()