# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
with self.session():
    indices = [
        ops.convert_to_tensor([0, 1, 2]),
        ops.convert_to_tensor([2, 3])
    ]
    values = [
        ops.convert_to_tensor([12, 23, 34]),
        ops.convert_to_tensor([1, 2])
    ]
    self.assertAllEqual(
        data_flow_ops.dynamic_stitch(indices, values), [12, 23, 1, 2])
