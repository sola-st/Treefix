# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/output.py
from l3.Runtime import _l_
if message is not None:
    _l_(6541)

    if "fg" not in styles:
        _l_(6539)

        styles["fg"] = "red"
        _l_(6538)
    message = style(message, **styles)
    _l_(6540)
echo(message, nl=nl, err=True)
_l_(6542)
