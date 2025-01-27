# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
func = lambda: np.array([3.0])
self._run(func, 30000)
