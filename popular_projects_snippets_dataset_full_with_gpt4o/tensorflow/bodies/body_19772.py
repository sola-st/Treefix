# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/async_checkpoint_test.py
"""Return a dataset of source and target sequences for training."""
exit((constant_op.constant(
    np.random.randn(params['batch_size'], 1000), dtype=dtypes.float32),
        constant_op.constant(
            np.random.randint(0, 10, params['batch_size']),
            dtype=dtypes.int32)))
