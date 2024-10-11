# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
dtype = CategoricalDtype(["a", "b"], ordered=True)
msg = "Cannot specify `categories` or `ordered` together with `dtype`."
with pytest.raises(ValueError, match=msg):
    Categorical(["a", "b"], categories=["a", "b"], dtype=dtype)

with pytest.raises(ValueError, match=msg):
    Categorical(["a", "b"], ordered=True, dtype=dtype)

with pytest.raises(ValueError, match=msg):
    Categorical(["a", "b"], ordered=False, dtype=dtype)
