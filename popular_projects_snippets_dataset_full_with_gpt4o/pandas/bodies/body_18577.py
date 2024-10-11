# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_to_offset.py
# see gh-13930

# We escape string because some of our
# inputs contain regex special characters.
msg = re.escape(f"Invalid frequency: {freqstr}")
with pytest.raises(ValueError, match=msg):
    to_offset(freqstr)
