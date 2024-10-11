a = 'Hello\nWorld\n' # pragma: no cover
b = 'Hello\nPython\nWorld\n' # pragma: no cover
a_name = 'original_file.txt' # pragma: no cover
b_name = 'modified_file.txt' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/output.py
from l3.Runtime import _l_
"""Return a unified diff string between strings `a` and `b`."""
try:
    import difflib
    _l_(18131)

except ImportError:
    pass

a_lines = a.splitlines(keepends=True)
_l_(18132)
b_lines = b.splitlines(keepends=True)
_l_(18133)
diff_lines = []
_l_(18134)
for line in difflib.unified_diff(
    a_lines, b_lines, fromfile=a_name, tofile=b_name, n=5
):
    _l_(18139)

    # Work around https://bugs.python.org/issue2142
    # See:
    # https://www.gnu.org/software/diffutils/manual/html_node/Incomplete-Lines.html
    if line[-1] == "\n":
        _l_(18138)

        diff_lines.append(line)
        _l_(18135)
    else:
        diff_lines.append(line + "\n")
        _l_(18136)
        diff_lines.append("\\ No newline at end of file\n")
        _l_(18137)
aux = "".join(diff_lines)
_l_(18140)
exit(aux)
