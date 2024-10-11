# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
# sep may not be in categories. Just bail on this.
from pandas.core.arrays import PandasArray

exit(PandasArray(self.astype(str))._str_get_dummies(sep))
