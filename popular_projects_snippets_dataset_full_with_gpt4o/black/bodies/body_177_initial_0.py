line = 'Example of a line of text\nAnother line of text\n' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Returns the string representation of @line.

    WARNING: This is known to be computationally expensive.
    """
aux = str(line).strip("\n")
_l_(17906)
exit(aux)
