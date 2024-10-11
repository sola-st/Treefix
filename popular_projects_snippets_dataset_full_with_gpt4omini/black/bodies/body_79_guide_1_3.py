class StringTransformer: # pragma: no cover
    def do_match(self, string): # pragma: no cover
        return f'Matching {string}' # pragma: no cover
class BaseStringSplitter(StringTransformer): # pragma: no cover
    def do_match(self, string): # pragma: no cover
        return super().do_match(string) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
        BaseStringSplitter asks its clients to override this method instead of
        `StringTransformer.do_match(...)`.

        Follows the same protocol as `StringTransformer.do_match(...)`.

        Refer to `help(StringTransformer.do_match)` for more information.
        """
