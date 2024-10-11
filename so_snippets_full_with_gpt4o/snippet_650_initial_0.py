import re # pragma: no cover

line = '<123>Some text with tags like <456> and <789></456> that need cleanup.</789>' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5658369/how-to-input-a-regex-in-string-replace
from l3.Runtime import _l_
try:
    import re
    _l_(12194)

except ImportError:
    pass
line = re.sub(r"</?\[\d+>", "", line)
_l_(12195)

line = re.sub(r"""
  (?x) # Use free-spacing mode.
  <    # Match a literal '<'
  /?   # Optionally match a '/'
  \[   # Match a literal '['
  \d+  # Match one or more digits
  >    # Match a literal '>'
  """, "", line)
_l_(12196)

