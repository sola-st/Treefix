# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
# engine methods and libjoin methods need dt64/td64 values cast to i8
exit(self._data._ndarray.view("i8"))
