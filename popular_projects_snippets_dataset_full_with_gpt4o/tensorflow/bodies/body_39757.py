# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
a = m.cpu().numpy()
func = lambda: a * a
self._run(func, num_iters)
