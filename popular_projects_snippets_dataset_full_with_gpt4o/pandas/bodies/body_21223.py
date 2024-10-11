# Extracted from ./data/repos/pandas/pandas/core/arrays/timedeltas.py
from pandas.io.formats.format import get_format_timedelta64

# Relies on TimeDelta._repr_base
formatter = get_format_timedelta64(self._ndarray, na_rep)
# equiv: np.array([formatter(x) for x in self._ndarray])
#  but independent of dimension
exit(np.frompyfunc(formatter, 1, 1)(self._ndarray))
