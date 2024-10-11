# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH 31200

# The exact error message of datetime() depends on its version
msg1 = r"function missing required argument '(year|month|day)' \(pos [123]\)"
msg2 = r"Required argument '(year|month|day)' \(pos [123]\) not found"
msg = "|".join([msg1, msg2])

with pytest.raises(TypeError, match=msg):
    Timestamp(**kwargs)
