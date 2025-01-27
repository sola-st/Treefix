# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
# Do a bunch of random high dimensional reductions
np.random.seed(42)
for _ in range(20):
    rank = np.random.randint(4, 10 + 1)
    axes, = np.nonzero(np.random.randint(2, size=rank))
    shape = tuple(np.random.randint(1, 3 + 1, size=rank))
    data = np.random.randint(1024, size=shape)
    self._compareAll(data, axes)
# Check some particular axis patterns
for rank in 4, 7, 10:
    shape = tuple(np.random.randint(1, 3 + 1, size=rank))
    data = np.random.randint(1024, size=shape)
    for axes in ([], np.arange(rank), np.arange(0, rank, 2),
                 np.arange(1, rank, 2)):
        self._compareAll(data, axes)
