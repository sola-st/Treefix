# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
if hashable:
    self.assertIsInstance(b, collections.abc.Hashable)
    self.assertLen(set([a, b]), 2)
else:
    # TODO(gjn): Figure out how to make this work for tf.Tensor
    # self.assertNotIsInstance(b, collections.abc.Hashable)
    with self.assertRaisesRegex(TypeError, 'unhashable'):
        set([a, b])
