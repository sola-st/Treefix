import sys # pragma: no cover

docstring = """\n    This is a sample docstring.\n    It has multiple\n    lines of text,\n    some of which are indented.\n    """ # pragma: no cover
def lines_with_leading_tabs_expanded(docstring):# pragma: no cover
    return [line.expandtabs() for line in docstring.splitlines()] # pragma: no cover
prefix = "" # pragma: no cover
sys.maxsize = 9223372036854775807 # pragma: no cover

import sys # pragma: no cover

docstring = """This is a sample docstring.\n    It has multiple\n    lines of text,\n    some of which are indented.""" # pragma: no cover
def lines_with_leading_tabs_expanded(docstring):# pragma: no cover
    return [line.expandtabs() for line in docstring.splitlines()] # pragma: no cover
prefix = "" # pragma: no cover
sys = type('Mock', (object,), {'maxsize': 9223372036854775807})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/strings.py
# https://www.python.org/dev/peps/pep-0257/#handling-docstring-indentation
from l3.Runtime import _l_
if not docstring:
    _l_(16240)

    aux = ""
    _l_(16239)
    exit(aux)
lines = lines_with_leading_tabs_expanded(docstring)
_l_(16241)
# Determine minimum indentation (first line doesn't count):
indent = sys.maxsize
_l_(16242)
for line in lines[1:]:
    _l_(16246)

    stripped = line.lstrip()
    _l_(16243)
    if stripped:
        _l_(16245)

        indent = min(indent, len(line) - len(stripped))
        _l_(16244)
trimmed = [lines[0].strip()]
_l_(16247)
if indent < sys.maxsize:
    _l_(16254)

    last_line_idx = len(lines) - 2
    _l_(16248)
    for i, line in enumerate(lines[1:]):
        _l_(16253)

        stripped_line = line[indent:].rstrip()
        _l_(16249)
        if stripped_line or i == last_line_idx:
            _l_(16252)

            trimmed.append(prefix + stripped_line)
            _l_(16250)
        else:
            trimmed.append("")
            _l_(16251)
aux = "\n".join(trimmed)
_l_(16255)
exit(aux)
