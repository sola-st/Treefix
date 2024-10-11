# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_contextlib_test.py
argspec = tf_inspect.getargspec(test_params_and_defaults)
self.assertEqual(['a', 'b', 'c', 'd'], argspec.args)
self.assertEqual((2, True, 'hello'), argspec.defaults)
