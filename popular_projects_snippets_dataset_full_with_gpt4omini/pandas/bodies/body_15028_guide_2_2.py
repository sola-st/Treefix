import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas import DataFrame, to_datetime # pragma: no cover
import pandas._testing as tm # pragma: no cover

df = pd.DataFrame(np.random.randn(100, 2)) # pragma: no cover
df[2] = to_datetime(np.random.randint(812419200000000000, 819331200000000000, size=100, dtype=np.int64)) # pragma: no cover
_check_plot_works = lambda f, default_axes: f() # pragma: no cover
tm = type('Mock', (object,), {'close': lambda: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
from l3.Runtime import _l_
df = DataFrame(np.random.randn(100, 2))
_l_(10772)
df[2] = to_datetime(
    np.random.randint(
        812419200000000000,
        819331200000000000,
        size=100,
        dtype=np.int64,
    )
)
_l_(10773)
# Use default_axes=True when plotting method generate subplots itself
_check_plot_works(df.hist, default_axes=True)
_l_(10774)
self.plt.tight_layout()
_l_(10775)

tm.close()
_l_(10776)
