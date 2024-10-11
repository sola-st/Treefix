# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
result = algos.value_counts([1, 1.0])
assert len(result) == 1

result = algos.value_counts([1, 1.0], bins=1)
assert len(result) == 1

result = algos.value_counts(Series([1, 1.0, "1"]))  # object
assert len(result) == 2

msg = "bins argument only works with numeric data"
with pytest.raises(TypeError, match=msg):
    algos.value_counts(["1", 1], bins=1)
