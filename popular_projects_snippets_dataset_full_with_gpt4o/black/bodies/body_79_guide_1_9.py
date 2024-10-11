from typing import Any # pragma: no cover
class StringTransformer: # pragma: no cover
    def do_match(self, string: str) -> bool: # pragma: no cover
        return True # pragma: no cover
class BaseStringSplitter(StringTransformer): # pragma: no cover
    def do_match(self, string: str) -> bool: # pragma: no cover
        # Example implementation of overriding do_match # pragma: no cover
        return ' ' in string # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
        BaseStringSplitter asks its clients to override this method instead of
        `StringTransformer.do_match(...)`.

        Follows the same protocol as `StringTransformer.do_match(...)`.

        Refer to `help(StringTransformer.do_match)` for more information.
        """
