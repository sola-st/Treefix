# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
df = DataFrame({"A": ["a", "a", "b", "c"]})
xpr = f"Expected an instance of {cls.__name__}"
with pytest.raises(TypeError, match=xpr):
    df.astype({"A": cls})

with pytest.raises(TypeError, match=xpr):
    df["A"].astype(cls)
