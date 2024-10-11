from typing import Optional, Union # pragma: no cover

axes = 0 # pragma: no cover
class MockObj:  # Mock object to simulate behavior# pragma: no cover
    def __init__(self, ndim):# pragma: no cover
        self.ndim = ndim# pragma: no cover
        self.method = 'get'# pragma: no cover
    def get(self, axified):# pragma: no cover
        return 'Mocked value'# pragma: no cover
obj = MockObj(2) # pragma: no cover
method = 'get' # pragma: no cover
key = slice(1, 3) # pragma: no cover
fails = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexing/common.py
from l3.Runtime import _l_
if axes is None:
    _l_(6555)

    axes_list = [0, 1]
    _l_(6552)
else:
    assert axes in [0, 1]
    _l_(6553)
    axes_list = [axes]
    _l_(6554)

for ax in axes_list:
    _l_(6567)

    if ax < obj.ndim:
        _l_(6566)

        # create a tuple accessor
        new_axes = [slice(None)] * obj.ndim
        _l_(6556)
        new_axes[ax] = key
        _l_(6557)
        axified = tuple(new_axes)
        _l_(6558)
        try:
            _l_(6565)

            getattr(obj, method).__getitem__(axified)
            _l_(6559)
        except (IndexError, TypeError, KeyError) as detail:
            _l_(6564)

            # if we are in fails, the ok, otherwise raise it
            if fails is not None:
                _l_(6562)

                if isinstance(detail, fails):
                    _l_(6561)

                    exit()
                    _l_(6560)
            raise
            _l_(6563)
