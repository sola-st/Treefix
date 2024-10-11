# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/padding_fifo_queue_test.py
with self.cached_session():
    with self.assertRaisesRegex(
        ValueError,
        r"When providing partial shapes, a list of shapes must be provided."):
        self.evaluate(
            data_flow_ops.PaddingFIFOQueue(10, dtypes_lib.float32,
                                           None).queue_ref)
