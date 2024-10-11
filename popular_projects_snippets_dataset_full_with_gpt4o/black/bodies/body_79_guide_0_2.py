from typing import Any # pragma: no cover
class StringTransformer: # pragma: no cover
    def do_match(self, *args: Any, **kwargs: Any) -> bool: # pragma: no cover
        # Mock implementation # pragma: no cover
        return True # pragma: no cover
class BaseStringSplitter(StringTransformer): # pragma: no cover
    def do_match(self, *args: Any, **kwargs: Any) -> bool: # pragma: no cover
        # Detailed implementation here # pragma: no cover
        return super().do_match(*args, **kwargs) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
        BaseStringSplitter asks its clients to override this method instead of
        `StringTransformer.do_match(...)`.

        Follows the same protocol as `StringTransformer.do_match(...)`.

        Refer to `help(StringTransformer.do_match)` for more information.
        """
