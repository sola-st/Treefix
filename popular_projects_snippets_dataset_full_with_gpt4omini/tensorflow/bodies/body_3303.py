# Extracted from ./data/repos/tensorflow/tensorflow/core/platform/ram_file_system_test.py
batch_size = 128
exit((constant_op.constant(np.random.randn(batch_size, 100),
                             dtype=dtypes.float32),
        constant_op.constant(np.random.randn(batch_size, 1),
                             dtype=dtypes.float32)))
