import json # pragma: no cover
from difflib import unified_diff # pragma: no cover

a = '{"cells": [{"cell_type": "code", "source": ["print(\"Hello World\")\n"]}]}' # pragma: no cover
b = '{"cells": [{"cell_type": "code", "source": ["print(\"Hello Universe\")\n"]}]}' # pragma: no cover
def diff(a, b, fromfile, tofile): return "\n".join(unified_diff(a.splitlines(), b.splitlines(), fromfile=fromfile, tofile=tofile)) # pragma: no cover
a_name = "Notebook_A" # pragma: no cover
b_name = "Notebook_B" # pragma: no cover

import json # pragma: no cover
from difflib import unified_diff # pragma: no cover

a = '{"cells": [{"cell_type": "code", "source": ["print(\\\"Hello World\\\")\\n"]}]}' # pragma: no cover
b = '{"cells": [{"cell_type": "code", "source": ["print(\\\"Hello Universe\\\")\\n"]}]}' # pragma: no cover
def diff(a, b, fromfile, tofile): return "\n".join(unified_diff(a.splitlines(), b.splitlines(), fromfile=fromfile, tofile=tofile)) # pragma: no cover
a_name = "Notebook_A" # pragma: no cover
b_name = "Notebook_B" # pragma: no cover

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
