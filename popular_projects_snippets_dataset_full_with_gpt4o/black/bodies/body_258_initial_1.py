import json # pragma: no cover
import difflib # pragma: no cover

a = '{"cells": [{"cell_type": "code", "source": ["print(\"Hello World\")"]}, {"cell_type": "code", "source": ["x = 2 + 2"]}]}' # pragma: no cover
b = '{"cells": [{"cell_type": "code", "source": ["print(\"Hello Universe\")"]}, {"cell_type": "code", "source": ["x = 3 + 2"]}]}' # pragma: no cover
def diff(a, b, a_name, b_name): return '\n'.join(difflib.unified_diff(a.splitlines(keepends=True), b.splitlines(keepends=True), fromfile=a_name, tofile=b_name)) # pragma: no cover
a_name = 'notebook_a' # pragma: no cover
b_name = 'notebook_b' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/output.py
from l3.Runtime import _l_
"""Return a unified diff string between each cell in notebooks `a` and `b`."""
a_nb = json.loads(a)
_l_(18902)
b_nb = json.loads(b)
_l_(18903)
diff_lines = [
    diff(
        "".join(a_nb["cells"][cell_number]["source"]) + "\n",
        "".join(b_nb["cells"][cell_number]["source"]) + "\n",
        f"{a_name}:cell_{cell_number}",
        f"{b_name}:cell_{cell_number}",
    )
    for cell_number, cell in enumerate(a_nb["cells"])
    if cell["cell_type"] == "code"
]
_l_(18904)
aux = "".join(diff_lines)
_l_(18905)
exit(aux)
