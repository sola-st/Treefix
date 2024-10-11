# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/output.py
from l3.Runtime import _l_
if message is not None:
    _l_(18313)

    if "fg" not in styles:
        _l_(18311)

        styles["fg"] = "red"
        _l_(18310)
    message = style(message, **styles)
    _l_(18312)
echo(message, nl=nl, err=True)
_l_(18314)
