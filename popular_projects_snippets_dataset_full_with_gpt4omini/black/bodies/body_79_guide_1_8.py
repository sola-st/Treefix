class BaseStringSplitter: # pragma: no cover
    def do_match(self): # pragma: no cover
        raise NotImplementedError('Subclasses should implement this!') # pragma: no cover
class StringTransformer(BaseStringSplitter): # pragma: no cover
    def do_match(self): # pragma: no cover
        return 'StringTransformer do_match executed' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
        BaseStringSplitter asks its clients to override this method instead of
        `StringTransformer.do_match(...)`.

        Follows the same protocol as `StringTransformer.do_match(...)`.

        Refer to `help(StringTransformer.do_match)` for more information.
        """
