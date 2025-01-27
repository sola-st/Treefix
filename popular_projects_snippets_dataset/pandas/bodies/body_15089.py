# Extracted from ./data/repos/pandas/pandas/tests/base/test_conversion.py
idx = pd.MultiIndex.from_product([["A"], ["a", "b"]])
msg = "MultiIndex has no single backing array"
with pytest.raises(ValueError, match=msg):
    idx.array
