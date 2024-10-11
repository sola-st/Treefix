# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_invalid.py
# generator ok though
concat(DataFrame(np.random.rand(5, 5)) for _ in range(3))
