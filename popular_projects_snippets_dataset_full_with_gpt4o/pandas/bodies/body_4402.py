# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# can't cast to float
test_data = {
    "A": dict(zip(range(20), tm.makeStringIndex(20))),
    "B": dict(zip(range(15), np.random.randn(15))),
}
with pytest.raises(ValueError, match="could not convert string"):
    DataFrame(test_data, dtype=float)
