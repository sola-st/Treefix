# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_time.py
new_string = "14.15"
msg = r"Cannot convert arg \['14\.15'\] to a time"
if not PY311:
    with pytest.raises(ValueError, match=msg):
        to_time(new_string)
assert to_time(new_string, format="%H.%M") == time(14, 15)
