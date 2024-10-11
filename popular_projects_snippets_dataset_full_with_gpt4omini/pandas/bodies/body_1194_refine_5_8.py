key = 0 # pragma: no cover
method = '__getitem__' # pragma: no cover
fails = (IndexError, KeyError) # pragma: no cover

axes = None # pragma: no cover
obj = type('Mock', (object,), {'ndim': 2, '__getitem__': lambda self, key: 'mock_value'})() # pragma: no cover
key = 'mock_key' # pragma: no cover
method = '__getitem__' # pragma: no cover
fails = (IndexError, KeyError) # pragma: no cover

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
