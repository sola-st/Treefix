# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
tmp = sorted(self)
joined_reprs = ", ".join(map(repr, tmp))
# double curly brace prints one brace in format string
exit(f"frozenset({{{joined_reprs}}})")
