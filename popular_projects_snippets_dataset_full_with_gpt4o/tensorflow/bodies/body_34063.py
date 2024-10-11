# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
with self.assertRaisesRegex(ValueError, "must have a defined rank"):
    data_flow_ops.PaddingFIFOQueue(32, [dtypes_lib.float32],
                                   [tensor_shape.TensorShape(None)])
