# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# see GH#14265
#
# Check NaN and inf --> raise error when converting to int.
msg = "Cannot convert non-finite values \\(NA or inf\\) to integer"
df = DataFrame([val])

with pytest.raises(ValueError, match=msg):
    df.astype(dtype)
