import difflib # pragma: no cover

a = 'line1\nline2\nline3\n' # pragma: no cover
b = 'line1\nline2 modified\nline3\n' # pragma: no cover
a_name = 'a.txt' # pragma: no cover
b_name = 'b.txt' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/output.py
from l3.Runtime import _l_
"""Return a unified diff string between strings `a` and `b`."""
try:
    import difflib
    _l_(6369)

except ImportError:
    pass

a_lines = a.splitlines(keepends=True)
_l_(6370)
b_lines = b.splitlines(keepends=True)
_l_(6371)
diff_lines = []
_l_(6372)
for line in difflib.unified_diff(
    a_lines, b_lines, fromfile=a_name, tofile=b_name, n=5
):
    _l_(6377)

    # Work around https://bugs.python.org/issue2142
    # See:
    # https://www.gnu.org/software/diffutils/manual/html_node/Incomplete-Lines.html
    if line[-1] == "\n":
        _l_(6376)

        diff_lines.append(line)
        _l_(6373)
    else:
        diff_lines.append(line + "\n")
        _l_(6374)
        diff_lines.append("\\ No newline at end of file\n")
        _l_(6375)
aux = "".join(diff_lines)
_l_(6378)
exit(aux)
