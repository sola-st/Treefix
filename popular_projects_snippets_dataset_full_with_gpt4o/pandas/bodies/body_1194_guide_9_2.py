import numpy as np # pragma: no cover

axes = 1 # pragma: no cover
obj = type('Mock', (object,), {'ndim': 2, '__getitem__': lambda self, key: (_ for _ in ()).throw(IndexError)})() # pragma: no cover
key = slice(None, None) # pragma: no cover
method = '__getitem__' # pragma: no cover
fails = IndexError # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexing/common.py
from l3.Runtime import _l_
if axes is None:
    _l_(16820)

    axes_list = [0, 1]
    _l_(16817)
else:
    assert axes in [0, 1]
    _l_(16818)
    axes_list = [axes]
    _l_(16819)

for ax in axes_list:
    _l_(16832)

    if ax < obj.ndim:
        _l_(16831)

        # create a tuple accessor
        new_axes = [slice(None)] * obj.ndim
        _l_(16821)
        new_axes[ax] = key
        _l_(16822)
        axified = tuple(new_axes)
        _l_(16823)
        try:
            _l_(16830)

            getattr(obj, method).__getitem__(axified)
            _l_(16824)
        except (IndexError, TypeError, KeyError) as detail:
            _l_(16829)

            # if we are in fails, the ok, otherwise raise it
            if fails is not None:
                _l_(16827)

                if isinstance(detail, fails):
                    _l_(16826)

                    exit()
                    _l_(16825)
            raise
            _l_(16828)
