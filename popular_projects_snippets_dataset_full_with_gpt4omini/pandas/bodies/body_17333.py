# Extracted from ./data/repos/pandas/pandas/tests/generic/test_finalize.py
pytest.importorskip("numexpr")
df = pd.DataFrame({"A": [1, 2]})
df.attrs["A"] = 1
result = df.eval("A + 1", engine="numexpr")
assert result.attrs == {"A": 1}
