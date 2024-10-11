from typing import Optional # pragma: no cover

def convert_one_fmt_off_pair(node: str, preview: Optional[bool] = False) -> bool: return False # pragma: no cover
node = 'This is a sample node.' # pragma: no cover
preview = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/comments.py
from l3.Runtime import _l_
"""Convert content between `# fmt: off`/`# fmt: on` into standalone comments."""
try_again = True
_l_(4290)
while try_again:
    _l_(4292)

    try_again = convert_one_fmt_off_pair(node, preview=preview)
    _l_(4291)
