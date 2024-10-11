import json # pragma: no cover
from difflib import unified_diff # pragma: no cover

a = '{"cells": [{"cell_type": "code", "source": ["print(\"Hello World\")"]}, {"cell_type": "markdown", "source": ["# Heading"]}, {"cell_type": "code", "source": ["x = 1 + 1\nprint(x)"]}]}' # pragma: no cover
b = '{"cells": [{"cell_type": "code", "source": ["print(\"Hello World!\")"]}, {"cell_type": "markdown", "source": ["# Heading"]}, {"cell_type": "code", "source": ["x = 2 + 2\nprint(x)"]}]}' # pragma: no cover
def diff(a_source, b_source, a_label, b_label):# pragma: no cover
    diff_lines = list(unified_diff(a_source.splitlines(keepends=True), b_source.splitlines(keepends=True), fromfile=a_label, tofile=b_label))# pragma: no cover
    return "\n".join(diff_lines) + "\n" # pragma: no cover
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
