# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/test_util.py
outputs = self._run_targets(targets1, targets2)
outputs = nest.flatten(outputs)  # flatten SparseTensorValues
n = len(outputs) // 2
for i in range(n):
    if outputs[i + n].dtype != np.object_:
        self.assertAllClose(outputs[i + n], outputs[i], rtol=rtol, atol=atol)
    else:
        self.assertAllEqual(outputs[i + n], outputs[i])
