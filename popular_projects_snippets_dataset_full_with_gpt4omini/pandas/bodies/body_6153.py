# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
# GH 24382
err_msg = "attempt to get"
with pytest.raises(ValueError, match=err_msg):
    getattr(data[:0], method)()
