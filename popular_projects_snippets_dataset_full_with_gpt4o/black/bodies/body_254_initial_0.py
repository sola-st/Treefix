from typing import Dict # pragma: no cover
from typing import Callable # pragma: no cover
import click # pragma: no cover

message = 'Hello, World!' # pragma: no cover
styles = {} # pragma: no cover
def style(msg: str, **kwargs: Dict[str, bool]) -> str:# pragma: no cover
    if kwargs.get('bold', False):# pragma: no cover
        return f'**{msg}**'# pragma: no cover
    return msg # pragma: no cover
def echo(msg: str, nl: bool, err: bool):# pragma: no cover
    click.echo(msg, nl=nl, err=err) # pragma: no cover
nl = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/output.py
from l3.Runtime import _l_
if message is not None:
    _l_(17617)

    if "bold" not in styles:
        _l_(17615)

        styles["bold"] = True
        _l_(17614)
    message = style(message, **styles)
    _l_(17616)
echo(message, nl=nl, err=True)
_l_(17618)
