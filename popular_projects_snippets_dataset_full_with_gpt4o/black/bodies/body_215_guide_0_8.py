import sys # pragma: no cover

content = ' ' # pragma: no cover
COMMENT_EXCEPTIONS = {'preview': ['##', '#!', '#:', '#']} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/comments.py
from l3.Runtime import _l_
"""Return a consistently formatted comment from the given `content` string.

    All comments (except for "##", "#!", "#:", '#'") should have a single
    space between the hash sign and the content.

    If `content` didn't start with a hash sign, one is provided.
    """
content = content.rstrip()
_l_(19588)
if not content:
    _l_(19590)

    aux = "#"
    _l_(19589)
    exit(aux)

if content[0] == "#":
    _l_(19592)

    content = content[1:]
    _l_(19591)
NON_BREAKING_SPACE = " "
_l_(19593)
if (
    content
    and content[0] == NON_BREAKING_SPACE
    and not content.lstrip().startswith("type:")
):
    _l_(19595)

    content = " " + content[1:]  # Replace NBSP by a simple space
    _l_(19594)  # Replace NBSP by a simple space
if content and content[0] not in COMMENT_EXCEPTIONS[preview]:
    _l_(19597)

    content = " " + content
    _l_(19596)
aux = "#" + content
_l_(19598)
exit(aux)
