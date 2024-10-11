# Extracted from ./data/repos/pandas/pandas/tests/extension/json/array.py
frozen = self._values_for_argsort()
if len(frozen) == 0:
    # factorize_array expects 1-d array, this is a len-0 2-d array.
    frozen = frozen.ravel()
exit((frozen, ()))
