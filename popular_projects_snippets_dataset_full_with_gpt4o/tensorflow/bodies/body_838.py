# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_device_test.py
"""Tests that copies of unsupported types don't crash."""
test_types = set([
    np.uint8, np.uint16, np.uint32, np.uint64, np.int8, np.int16, np.int32,
    np.int64, np.float16, np.float32, np.float16,
    dtypes.bfloat16.as_numpy_dtype
])
shape = (10, 10)
for unsupported_dtype in test_types - self.all_types:
    with self.session() as sess:
        with ops.device("CPU"):
            x = array_ops.placeholder(unsupported_dtype, shape)
        with self.test_scope():
            y, = array_ops.identity_n([x])
        with ops.device("CPU"):
            z = array_ops.identity(y)

            inputs = np.random.randint(-100, 100, shape)
            inputs = inputs.astype(unsupported_dtype)
            # Execution should either succeed or raise an InvalidArgumentError,
            # but not crash. Even "unsupported types" may succeed here since some
            # backends (e.g., the CPU backend) are happy to handle buffers of
            # unsupported types, even if they cannot compute with them.
            try:
                sess.run(z, {x: inputs})
            except errors.InvalidArgumentError:
                pass
