# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
assert float_frame.to_json() == float_frame.to_json(orient="columns")
