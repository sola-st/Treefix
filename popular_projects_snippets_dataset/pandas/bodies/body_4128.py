# Extracted from ./data/repos/pandas/pandas/tests/frame/test_iteration.py
df = DataFrame([[1, 2, 3], [4, 5, 6]], columns=["a", "a", "b"])
for k, v in df.items():
    assert isinstance(v, DataFrame._constructor_sliced)
