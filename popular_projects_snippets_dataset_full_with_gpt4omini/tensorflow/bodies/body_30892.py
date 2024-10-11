# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
with self.session(use_gpu=False):
    indices = [
        ops.convert_to_tensor([0, 1, 5, 6, 7]),
        ops.convert_to_tensor([2, 4, 3])
    ]
    values = [
        ops.convert_to_tensor([12, 23, 34, 45, 56]),
        ops.convert_to_tensor([1, 3, 2])
    ]
    self.assertAllEqual(
        data_flow_ops.parallel_dynamic_stitch(indices, values),
        [12, 23, 1, 2, 3, 34, 45, 56])
