# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rename.py
df = DataFrame(columns=["A", "B", "C", "D"])
with pytest.raises(KeyError, match="'E'] not found in axis"):
    df.rename(columns={"A": "a", "E": "e"}, errors="raise")
