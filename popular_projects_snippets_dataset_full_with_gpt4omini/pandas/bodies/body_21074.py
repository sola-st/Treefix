# Extracted from ./data/repos/pandas/pandas/core/arrays/string_.py
values = extract_array(values)

super().__init__(values, copy=copy)
if not isinstance(values, type(self)):
    self._validate()
NDArrayBacked.__init__(self, self._ndarray, StringDtype(storage="python"))
