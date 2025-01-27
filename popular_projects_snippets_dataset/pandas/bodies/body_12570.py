# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
df = DataFrame([{"a_float": value}])
encoded = df.to_json(double_precision=precision)
assert encoded == f'{{"a_float":{{"0":{expected_val}}}}}'
