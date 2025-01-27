# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
# GH7222
from pandas.tseries.offsets import CustomBusinessDay

s = Series(
    range(100, 121),
    index=pd.bdate_range(
        start="2014-05-01",
        end="2014-06-01",
        freq=CustomBusinessDay(holidays=["2014-05-26"]),
    ),
)

_check_plot_works(s.plot)
