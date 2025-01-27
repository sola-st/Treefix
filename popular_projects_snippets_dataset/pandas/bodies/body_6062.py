# Extracted from ./data/repos/pandas/pandas/tests/extension/base/ops.py
ser = pd.Series(data)
self._check_divmod_op(ser, divmod, data)

other = data_for_twos
self._check_divmod_op(other, ops.rdivmod, ser)

other = pd.Series(other)
self._check_divmod_op(other, ops.rdivmod, ser)
