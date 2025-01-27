# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
with self.session(use_gpu=False):
    indices = [
        ops.convert_to_tensor([0, 1, 4, 6]),
        ops.convert_to_tensor([2, 3, 5])
    ]
    values = [
        ops.convert_to_tensor([12, 23, 34, 45]),
        ops.convert_to_tensor([1, 2, 3])
    ]
    self.assertAllEqual(
        data_flow_ops.parallel_dynamic_stitch(indices, values),
        [12, 23, 1, 2, 34, 3, 45])
