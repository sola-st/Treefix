content = '# This is a sample comment' # pragma: no cover
COMMENT_EXCEPTIONS = ['##', '#!', '#:', '#'] # pragma: no cover
preview = 0 # pragma: no cover

content = '# This is a comment' # pragma: no cover
COMMENT_EXCEPTIONS = ['##', '#!', '#:', '#'] # pragma: no cover
preview = 'preview' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/comments.py
from l3.Runtime import _l_
"""Return a consistently formatted comment from the given `content` string.

    All comments (except for "##", "#!", "#:", '#'") should have a single
    space between the hash sign and the content.

    If `content` didn't start with a hash sign, one is provided.
    """
content = content.rstrip()
_l_(8173)
if not content:
    _l_(8175)

    aux = "#"
    _l_(8174)
    exit(aux)

if content[0] == "#":
    _l_(8177)

    content = content[1:]
    _l_(8176)
NON_BREAKING_SPACE = " "
_l_(8178)
if (
    content
    and content[0] == NON_BREAKING_SPACE
    and not content.lstrip().startswith("type:")
):
    _l_(8180)

    content = " " + content[1:]  # Replace NBSP by a simple space
    _l_(8179)  # Replace NBSP by a simple space
if content and content[0] not in COMMENT_EXCEPTIONS[preview]:
    _l_(8182)

    content = " " + content
    _l_(8181)
aux = "#" + content
_l_(8183)
exit(aux)
