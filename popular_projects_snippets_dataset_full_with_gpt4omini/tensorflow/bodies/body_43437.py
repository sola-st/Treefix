# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py
decorators, _ = tf_decorator.unwrap(test_function)
self.assertEqual(0, len(decorators))
