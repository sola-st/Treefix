# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
from l3.Runtime import _l_
df = DataFrame(np.random.randn(100, 2))
_l_(22167)
df[2] = to_datetime(
    np.random.randint(
        812419200000000000,
        819331200000000000,
        size=100,
        dtype=np.int64,
    )
)
_l_(22168)
# Use default_axes=True when plotting method generate subplots itself
_check_plot_works(df.hist, default_axes=True)
_l_(22169)
self.plt.tight_layout()
_l_(22170)

tm.close()
_l_(22171)
