# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default():
    # Can't have vector `keep_input` with `enqueue_many=False`.
    with self.assertRaisesRegex(ValueError,
                                "`keep_input` cannot be a vector"):
        inp.maybe_shuffle_batch([array_ops.zeros(5)],
                                1,
                                10,
                                1,
                                keep_input=constant_op.constant([True, False]),
                                enqueue_many=False)
    # Can't have `keep_input` with more than one dimension.
    with self.assertRaisesRegex(ValueError, "must be 0 or 1 dimensions"):
        inp.maybe_shuffle_batch([array_ops.zeros(5)],
                                1,
                                10,
                                1,
                                keep_input=constant_op.constant([[True]]),
                                enqueue_many=True)
    # `keep_input` must have dimensions determined at graph construction.
    with self.assertRaisesRegex(ValueError,
                                "must be known at graph construction"):
        inp.maybe_shuffle_batch([array_ops.zeros(5)],
                                1,
                                10,
                                1,
                                keep_input=array_ops.placeholder(dtypes.bool),
                                enqueue_many=True)
