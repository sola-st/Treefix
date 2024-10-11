# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_dict.py
# GH#24939
df = DataFrame({(f"A_{i:d}"): [i] for i in range(256)})
result = df.to_dict("records")[0]
expected = {f"A_{i:d}": i for i in range(256)}
assert result == expected
