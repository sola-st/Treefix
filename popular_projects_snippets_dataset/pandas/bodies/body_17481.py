# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
# GH#18226
cls = tick_classes
# check that we cannot create e.g. Hour(weeks=3)
msg = rf"__init__\(\) got an unexpected keyword argument '{kwd}'"
with pytest.raises(TypeError, match=msg):
    cls(**{kwd: 3})
