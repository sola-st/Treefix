# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
# all missing with skipna=True is the same as empty
err_msg = "attempt to get"
data_na = type(data)._from_sequence([na_value, na_value], dtype=data.dtype)
with pytest.raises(ValueError, match=err_msg):
    getattr(data_na, method)()
