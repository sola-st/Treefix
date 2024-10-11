# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
# GH23843: Enhanced JSON normalize
output = nested_to_record(max_level_test_input_data, max_level=max_level)
assert output == expected
