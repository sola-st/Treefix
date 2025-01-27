# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_object.py
index = pd.Index(["a", "b", "c"])
# doesn't fail test unless there is a check before `+=`
assert "a" in index

index += "_x"
assert "a_x" in index
