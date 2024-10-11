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
