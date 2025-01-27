# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/integration_test/np_config_test.py
a = tf.constant(1.)

for name in {'T', 'astype', 'ravel', 'transpose', 'reshape', 'clip', 'size',
             'tolist'}:
    with self.assertRaisesRegex(AttributeError, 'enable_numpy_behavior'):
        getattr(a, name)

np_config.enable_numpy_behavior()

for name in {'T', 'astype', 'ravel', 'transpose', 'reshape', 'clip', 'size',
             'tolist'}:
    _ = getattr(a, name)
