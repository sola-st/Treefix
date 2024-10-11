# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
argspec = tf_inspect.getfullargspec(test_decorated_function_with_defaults)
self.assertEqual(['a', 'b', 'c'], argspec.args)
self.assertEqual((2, 'Hello'), argspec.defaults)
