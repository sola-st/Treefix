# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_dict.py
# GH#24940
df = DataFrame({str(i): [i] for i in range(5)})
result = set(df.to_dict("records")[0].keys())
expected = set(df.columns)
assert result == expected
