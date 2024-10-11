# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
batch_size = 3
height, width = 4, 4
np.random.seed(1)  # Make it reproducible.
inputs = np.random.uniform(size=(batch_size, height, width,
                                 3)).astype(np.float32)
inputs = constant_op.constant(inputs)

outputs = nn_ops.leaky_relu(inputs)
self.assertEqual(inputs.shape, outputs.shape)

inputs, outputs = self.evaluate([inputs, outputs])

self.assertGreaterEqual(outputs.min(), 0.0)
self.assertLessEqual(outputs.max(), 1.0)
self.assertAllClose(inputs, outputs)
