import re # pragma: no cover

STRING_PREFIX_RE = re.compile(r'([FBUu]*)(.*)') # pragma: no cover
s = 'FBstring_example' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/strings.py
from l3.Runtime import _l_
"""Make all string prefixes lowercase."""
match = STRING_PREFIX_RE.match(s)
_l_(4118)
assert match is not None, f"failed to match string {s!r}"
_l_(4119)
orig_prefix = match.group(1)
_l_(4120)
new_prefix = (
    orig_prefix.replace("F", "f")
    .replace("B", "b")
    .replace("U", "")
    .replace("u", "")
)
_l_(4121)

# Python syntax guarantees max 2 prefixes and that one of them is "r"
if len(new_prefix) == 2 and "r" != new_prefix[0].lower():
    _l_(4123)

    new_prefix = new_prefix[::-1]
    _l_(4122)
aux = f"{new_prefix}{match.group(2)}"
_l_(4124)
exit(aux)
