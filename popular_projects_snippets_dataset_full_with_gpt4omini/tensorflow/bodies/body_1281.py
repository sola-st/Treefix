# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    tensor = gen_random_ops.random_uniform((2, 2), dtypes.float32)
    row0 = tensor[0].numpy()
    row1 = tensor[1].numpy()
    # It should be very unlikely to rng to generate two equal rows.
    self.assertFalse((row0 == row1).all())
