# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
if isinstance(a, (list, tuple)):
    for entry_a, entry_b in zip(a, b):
        self.assertAllEqualNested(entry_a, entry_b)
else:
    self.assertAllEqual(a, b)
