contents = '--- a/file.txt\n+++ b/file.txt\n@@ -1,3 +1,3 @@\n-line 1\n line 2\n+line 3\n' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/output.py
from l3.Runtime import _l_
"""Inject the ANSI color codes to the diff."""
lines = contents.split("\n")
_l_(4277)
for i, line in enumerate(lines):
    _l_(4287)

    if line.startswith("+++") or line.startswith("---"):
        _l_(4285)

        line = "\033[1m" + line + "\033[0m"  # bold, reset
        _l_(4278)  # bold, reset
    elif line.startswith("@@"):
        _l_(4284)

        line = "\033[36m" + line + "\033[0m"  # cyan, reset
        _l_(4279)  # cyan, reset
    elif line.startswith("+"):
        _l_(4283)

        line = "\033[32m" + line + "\033[0m"  # green, reset
        _l_(4280)  # green, reset
    elif line.startswith("-"):
        _l_(4282)

        line = "\033[31m" + line + "\033[0m"  # red, reset
        _l_(4281)  # red, reset
    lines[i] = line
    _l_(4286)
aux = "\n".join(lines)
_l_(4288)
exit(aux)
