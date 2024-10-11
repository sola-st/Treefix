# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
# GH#19142 check that the calling the constructors without passing
# any keyword arguments produce valid offsets
cls = offset_types
cls()
