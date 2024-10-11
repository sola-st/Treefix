# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH#42137
with pytest.raises(ValueError, match="invalid literal"):
    Series(["True", "False", "True", pd.NA], dtype="Int64")
