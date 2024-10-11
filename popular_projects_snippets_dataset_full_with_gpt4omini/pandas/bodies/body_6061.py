# Extracted from ./data/repos/pandas/pandas/tests/extension/base/ops.py
ser = pd.Series(data)
self._check_divmod_op(ser, divmod, 1, exc=self.divmod_exc)
self._check_divmod_op(1, ops.rdivmod, ser, exc=self.divmod_exc)
