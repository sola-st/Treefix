# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
# https://github.com/pandas-dev/pandas/issues/12392
# Enforced in 2.0
df = DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
with pytest.raises(TypeError, match=r".* is ambiguous."):
    df.reindex([0, 1], ["A", "B", "C"])
