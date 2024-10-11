# Extracted from ./data/repos/pandas/pandas/tests/extension/base/interface.py
# GH-20735: EA's with .values attribute give problems with internal
# code, disallowing this for now until solved
assert not hasattr(data, "values")
assert not hasattr(data, "_values")
