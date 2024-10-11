# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
with self.session(use_gpu=False):
    indices = [
        ops.convert_to_tensor([0, 1, 2, 3]),
        ops.convert_to_tensor([2, 3])
    ]
    values = [
        ops.convert_to_tensor([2, 3, 5, 7]),
        ops.convert_to_tensor([1, 1])
    ]
    self.assertAllEqual(
        data_flow_ops.dynamic_stitch(indices, values), [2, 3, 1, 1])
