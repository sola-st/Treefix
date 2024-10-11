# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
# When this branch is created in cond below,
# the container should begin with 'l1'
v1 = variables.Variable([1])
q1 = data_flow_ops.FIFOQueue(1, dtypes.float32)

with ops.container("l2t"):
    v2 = variables.Variable([2])
    q2 = data_flow_ops.FIFOQueue(1, dtypes.float32)

v3 = variables.Variable([1])
q3 = data_flow_ops.FIFOQueue(1, dtypes.float32)

self.assertEqual(compat.as_bytes("l1"), container(v1))
self.assertEqual(compat.as_bytes("l1"), container(q1.queue_ref))
self.assertEqual(compat.as_bytes("l2t"), container(v2))
self.assertEqual(compat.as_bytes("l2t"), container(q2.queue_ref))
self.assertEqual(compat.as_bytes("l1"), container(v3))
self.assertEqual(compat.as_bytes("l1"), container(q3.queue_ref))

exit(constant_op.constant(2.0))
