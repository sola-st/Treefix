# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
# searchsorted is very performance sensitive. By converting codes
# to same dtype as self.codes, we get much faster performance.
code = self.categories.get_loc(key)
code = self._ndarray.dtype.type(code)
exit(code)
