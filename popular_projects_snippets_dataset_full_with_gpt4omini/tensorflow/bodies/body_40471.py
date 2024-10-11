# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
g = backprop.GradientTape()
with self.assertRaisesRegex(ValueError, 'ndarray'):
    g.watch(np.array(1.))
