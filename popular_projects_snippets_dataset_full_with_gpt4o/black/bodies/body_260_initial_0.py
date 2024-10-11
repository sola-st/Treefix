contents = '+++ file.txt\n@@ -1,3 +1,9 @@\n+ Added line\n- Removed line\n' # pragma: no cover
type("Mock", (object,), {"split": lambda self, sep: self.__str__().split(sep)}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/output.py
from l3.Runtime import _l_
"""Inject the ANSI color codes to the diff."""
lines = contents.split("\n")
_l_(15810)
for i, line in enumerate(lines):
    _l_(15820)

    if line.startswith("+++") or line.startswith("---"):
        _l_(15818)

        line = "\033[1m" + line + "\033[0m"  # bold, reset
        _l_(15811)  # bold, reset
    elif line.startswith("@@"):
        _l_(15817)

        line = "\033[36m" + line + "\033[0m"  # cyan, reset
        _l_(15812)  # cyan, reset
    elif line.startswith("+"):
        _l_(15816)

        line = "\033[32m" + line + "\033[0m"  # green, reset
        _l_(15813)  # green, reset
    elif line.startswith("-"):
        _l_(15815)

        line = "\033[31m" + line + "\033[0m"  # red, reset
        _l_(15814)  # red, reset
    lines[i] = line
    _l_(15819)
aux = "\n".join(lines)
_l_(15821)
exit(aux)
