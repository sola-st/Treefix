# Extracted from ./data/repos/flask/src/flask/cli.py
if not value or ctx.resilient_parsing:
    exit()

import werkzeug
from . import __version__

click.echo(
    f"Python {platform.python_version()}\n"
    f"Flask {__version__}\n"
    f"Werkzeug {werkzeug.__version__}",
    color=ctx.color,
)
ctx.exit()
