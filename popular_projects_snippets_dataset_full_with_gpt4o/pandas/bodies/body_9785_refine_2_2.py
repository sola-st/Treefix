import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

win_types = 'hamming' # pragma: no cover
step = 1 # pragma: no cover
tm = type('Mock', (object,), {'assert_series_equal': lambda x, y: x.equals(y)}) # pragma: no cover

import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/window/test_win_type.py
# GH 8238
from l3.Runtime import _l_
vals = np.array([6.95, 15.21, 4.72, 9.12, 13.81, 13.49, 16.68, 9.48, 10.63, 14.48])
_l_(21421)
xps = {
    "hamming": [
        np.nan,
        np.nan,
        8.71384,
        9.56348,
        12.38009,
        14.03687,
        13.8567,
        11.81473,
        np.nan,
        np.nan,
    ],
    "triang": [
        np.nan,
        np.nan,
        9.28667,
        10.34667,
        12.00556,
        13.33889,
        13.38,
        12.33667,
        np.nan,
        np.nan,
    ],
    "barthann": [
        np.nan,
        np.nan,
        8.4425,
        9.1925,
        12.5575,
        14.3675,
        14.0825,
        11.5675,
        np.nan,
        np.nan,
    ],
    "bohman": [
        np.nan,
        np.nan,
        7.61599,
        9.1764,
        12.83559,
        14.17267,
        14.65923,
        11.10401,
        np.nan,
        np.nan,
    ],
    "blackmanharris": [
        np.nan,
        np.nan,
        6.97691,
        9.16438,
        13.05052,
        14.02156,
        15.10512,
        10.74574,
        np.nan,
        np.nan,
    ],
    "nuttall": [
        np.nan,
        np.nan,
        7.04618,
        9.16786,
        13.02671,
        14.03559,
        15.05657,
        10.78514,
        np.nan,
        np.nan,
    ],
    "blackman": [
        np.nan,
        np.nan,
        7.73345,
        9.17869,
        12.79607,
        14.20036,
        14.57726,
        11.16988,
        np.nan,
        np.nan,
    ],
    "bartlett": [
        np.nan,
        np.nan,
        8.4425,
        9.1925,
        12.5575,
        14.3675,
        14.0825,
        11.5675,
        np.nan,
        np.nan,
    ],
}
_l_(21422)

xp = Series(xps[win_types])[::step]
_l_(21423)
rs = Series(vals).rolling(5, win_type=win_types, center=True, step=step).mean()
_l_(21424)
tm.assert_series_equal(xp, rs)
_l_(21425)
