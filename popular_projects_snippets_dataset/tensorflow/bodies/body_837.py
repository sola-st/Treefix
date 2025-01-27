# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_device_test.py
"""Tests that copies onto and off XLA devices work."""
shapes = [[0], [1], [1, 0], [1024, 0], [1024, 1], [3, 777], [777, 3],
          [16384, 1], [1, 16384], [1, 20000, 1, 1]]
for dtype in self.numeric_types:
    for shape in shapes:
        with self.session() as sess:
            with ops.device("CPU"):
                x = array_ops.placeholder(dtype, shape)
            with self.test_scope():
                y = x + x
            with ops.device("CPU"):
                z = array_ops.identity(y)

            inputs = np.random.randint(-100, 100, shape).astype(dtype)
            result = sess.run(z, {x: inputs})
        self.assertAllCloseAccordingToType(result, inputs + inputs)
