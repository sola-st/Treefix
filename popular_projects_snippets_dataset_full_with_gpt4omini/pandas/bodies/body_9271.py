# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
# https://github.com/pandas-dev/pandas/issues/16022
msg = r"^Parameter 'categories' must be list-like, was"
with pytest.raises(TypeError, match=msg):
    Categorical(["a", "b"], categories="a")
