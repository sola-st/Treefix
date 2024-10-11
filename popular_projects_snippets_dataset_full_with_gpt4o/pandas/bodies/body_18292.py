# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_object.py
# from bug report
index = pd.Index(["a", "b", "c"])
index2 = index + "foo"

assert "a" not in index2
assert "afoo" in index2
