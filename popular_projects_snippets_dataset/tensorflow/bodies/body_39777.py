# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
a = m.cpu().numpy()
b = a.T if transpose_b else a
func = lambda: np.dot(a, b)
self._run(func, num_iters)
