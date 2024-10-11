# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# dataframe with last column very wide -> check it is not used to
# determine size of truncation (...) column
df = DataFrame(
    {
        "a": [108480, 30830],
        "b": [12345, 12345],
        "c": [12345, 12345],
        "d": [12345, 12345],
        "e": ["a" * 50] * 2,
    }
)
assert "..." in str(df)
assert "    ...    " not in str(df)
