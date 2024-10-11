# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
# b/141166460
rt = RaggedTensor.from_value_rowids([1, 2, 3], [0, 0, 2])
c = array_ops.placeholder_with_default(True, None)
result = control_flow_ops.cond(c, lambda: rt, lambda: rt)
self.assertAllEqual(rt, result)
