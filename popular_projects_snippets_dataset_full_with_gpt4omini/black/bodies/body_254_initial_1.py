from typing import Dict, Callable, Optional # pragma: no cover

message = 'Hello, World!' # pragma: no cover
styles = {} # pragma: no cover
def style(text: str, **kwargs) -> str: return f'**{text}**' if kwargs.get('bold', False) else text # pragma: no cover
def echo(text: str, nl: bool = True, err: bool = False): print(text, end='\n' if nl else '') # pragma: no cover
nl = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/output.py
from l3.Runtime import _l_
if message is not None:
    _l_(5805)

    if "bold" not in styles:
        _l_(5803)

        styles["bold"] = True
        _l_(5802)
    message = style(message, **styles)
    _l_(5804)
echo(message, nl=nl, err=True)
_l_(5806)
