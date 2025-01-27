# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_first_valid_index.py
# GH#21441
df = DataFrame(data, index=idx)
assert expected_first == df.first_valid_index()
assert expected_last == df.last_valid_index()
