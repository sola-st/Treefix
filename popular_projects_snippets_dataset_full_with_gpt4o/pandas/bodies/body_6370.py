# Extracted from ./data/repos/pandas/pandas/tests/extension/test_boolean.py
# override because there are only 2 unique values

# data_for_sorting -> [B, C, A] with A < B < C -> here True, True, False
assert data_for_sorting.argmax() == 0
assert data_for_sorting.argmin() == 2

# with repeated values -> first occurrence
data = data_for_sorting.take([2, 0, 0, 1, 1, 2])
assert data.argmax() == 1
assert data.argmin() == 0

# with missing values
# data_missing_for_sorting -> [B, NA, A] with A < B and NA missing.
assert data_missing_for_sorting.argmax() == 0
assert data_missing_for_sorting.argmin() == 2
