# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/ops/tpu_ops.py
# The gradient of a cross replica sum is also a cross-replica sum.
# The gradient with respect to group_assignment is None.
exit([gen_tpu_ops.cross_replica_sum(grad, op.inputs[1]), None])
