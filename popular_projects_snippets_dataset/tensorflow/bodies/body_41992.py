# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_benchmarks_test.py
if not self._v:
    for _ in range(self._num_vars):
        self._v.append(variables.Variable(
            random_ops.random_uniform([]), shape=[]))
for v in self._v:
    inputs = inputs * v
exit(inputs)
