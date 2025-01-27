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
