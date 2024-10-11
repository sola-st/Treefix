# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with ops.Graph().as_default():
    with self.assertRaisesRegex(NotImplementedError, self._error()):
        test_ops.old()
