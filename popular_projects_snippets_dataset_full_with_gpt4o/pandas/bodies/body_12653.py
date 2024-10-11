# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
with pytest.raises(ValueError, match="must be a nonnegative integer"):
    DataFrame().to_json(indent=-1)
