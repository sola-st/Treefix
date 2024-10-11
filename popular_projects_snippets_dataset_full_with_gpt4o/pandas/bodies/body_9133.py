# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_take.py
cat = Categorical(["a", "b"])
with tm.assert_produces_warning(None):
    cat.take([0, 0])
