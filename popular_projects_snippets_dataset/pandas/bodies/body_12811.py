# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_readlines.py
df = DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
exit(df.to_json(lines=True, orient="records"))
