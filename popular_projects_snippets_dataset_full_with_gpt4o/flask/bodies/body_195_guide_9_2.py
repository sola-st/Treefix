s = 'some text' # pragma: no cover
kwargs = {} # pragma: no cover
try:# pragma: no cover
    # Begin code snippet# pragma: no cover
    """Deserialize data as JSON.# pragma: no cover
            :param s: Text or UTF-8 bytes.# pragma: no cover
            :param kwargs: May be passed to the underlying JSON library.# pragma: no cover
            """# pragma: no cover
    raise NotImplementedError # uncovered# pragma: no cover
    # End code snippet# pragma: no cover
except NotImplementedError as e:# pragma: no cover
    print(e) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
"""Deserialize data as JSON.

        :param s: Text or UTF-8 bytes.
        :param kwargs: May be passed to the underlying JSON library.
        """
raise NotImplementedError
_l_(22621)
