# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# see gh-15524, gh-15987
# as of 2.0 we raise on any non-supported unit rather than silently
#  cast to nanos; previously we only raised for frequencies higher
#  than ns
dtype = f"{kind}8[{unit}]"

msg = "dtype=.* is not supported. Supported resolutions are"
with pytest.raises(TypeError, match=msg):
    Series([], dtype=dtype)

with pytest.raises(TypeError, match=msg):
    # pre-2.0 the DataFrame cast raised but the Series case did not
    DataFrame([[0]], dtype=dtype)
