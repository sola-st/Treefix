# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
codes = pd.array([0, None], dtype="Int64")
categories = ["a", "b"]

msg = "codes cannot contain NA values"
with pytest.raises(ValueError, match=msg):
    Categorical.from_codes(codes, categories=categories)
