# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
values = []
for _ in range(1000):
    values.append(array_ops.zeros(shape=(1000,)))
self._run(lambda: np.array([x.numpy() for x in values]), 1000)
