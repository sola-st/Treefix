# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
# https://github.com/pandas-dev/pandas/issues/50787
ts = Timestamp("-2000-01-01")
msg = (
    "^strftime not yet supported on Timestamps which are outside the range of "
    "Python's standard library. For now, please call the components you need "
    r"\(such as `.year` and `.month`\) and construct your string from there.$"
)
with pytest.raises(NotImplementedError, match=msg):
    ts.strftime("%Y")
