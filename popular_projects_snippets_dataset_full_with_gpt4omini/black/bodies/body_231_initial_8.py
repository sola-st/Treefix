import sys # pragma: no cover

docstring = """This is an example docstring.""" # pragma: no cover
def lines_with_leading_tabs_expanded(docstring): return docstring.splitlines() # pragma: no cover
prefix = "    "  # Four spaces for indentation # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/strings.py
# https://www.python.org/dev/peps/pep-0257/#handling-docstring-indentation
from l3.Runtime import _l_
if not docstring:
    _l_(4487)

    aux = ""
    _l_(4486)
    exit(aux)
lines = lines_with_leading_tabs_expanded(docstring)
_l_(4488)
# Determine minimum indentation (first line doesn't count):
indent = sys.maxsize
_l_(4489)
for line in lines[1:]:
    _l_(4493)

    stripped = line.lstrip()
    _l_(4490)
    if stripped:
        _l_(4492)

        indent = min(indent, len(line) - len(stripped))
        _l_(4491)
trimmed = [lines[0].strip()]
_l_(4494)
if indent < sys.maxsize:
    _l_(4501)

    last_line_idx = len(lines) - 2
    _l_(4495)
    for i, line in enumerate(lines[1:]):
        _l_(4500)

        stripped_line = line[indent:].rstrip()
        _l_(4496)
        if stripped_line or i == last_line_idx:
            _l_(4499)

            trimmed.append(prefix + stripped_line)
            _l_(4497)
        else:
            trimmed.append("")
            _l_(4498)
aux = "\n".join(trimmed)
_l_(4502)
exit(aux)
