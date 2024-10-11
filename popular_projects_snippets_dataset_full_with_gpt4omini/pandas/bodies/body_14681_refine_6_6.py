import pandas as pd # pragma: no cover

DataFrame = pd.DataFrame # pragma: no cover
kwargs = {'by': 'c'} # pragma: no cover
self = type('Mock', (object,), {'_assert_xtickslabels_visibility': lambda self, axes, expected: None})() # pragma: no cover
expected = {'0': 'Label1', '1': 'Label2', '2': 'Label3'} # pragma: no cover

import pandas as pd # pragma: no cover

DataFrame = pd.DataFrame # pragma: no cover
kwargs = {'sharex': True} # pragma: no cover
self = type('Mock', (object,), {'_assert_xtickslabels_visibility': lambda self, axes, expected: None})() # pragma: no cover
expected = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_groupby.py
# https://github.com/pandas-dev/pandas/issues/20968
# sharex can now be switched check whether the right
# pair of axes is turned on or off

from l3.Runtime import _l_
df = DataFrame(
    {
        "a": [-1.43, -0.15, -3.70, -1.43, -0.14],
        "b": [0.56, 0.84, 0.29, 0.56, 0.85],
        "c": [0, 1, 2, 3, 1],
    },
    index=[0, 1, 2, 3, 4],
)
_l_(10568)
axes = df.groupby("c").boxplot(**kwargs)
_l_(10569)
self._assert_xtickslabels_visibility(axes, expected)
_l_(10570)
