# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iat.py

for i, row in enumerate(float_frame.index):
    for j, col in enumerate(float_frame.columns):
        result = float_frame.iat[i, j]
        expected = float_frame.at[row, col]
        assert result == expected
