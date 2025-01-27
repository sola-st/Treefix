# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
outputs = self._run_targets(targets1, targets2)
n = len(outputs) // 2
for i in range(n):
    self.assertAllEqual(outputs[i].shape, outputs[i + n].shape)
