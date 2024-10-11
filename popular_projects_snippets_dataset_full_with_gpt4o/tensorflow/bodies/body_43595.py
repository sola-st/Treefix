# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_contextlib_test.py
decorators, target = tf_decorator.unwrap(test_params_and_defaults)
self.assertEqual(1, len(decorators))
self.assertTrue(isinstance(decorators[0], tf_decorator.TFDecorator))
self.assertEqual('contextmanager', decorators[0].decorator_name)
self.assertFalse(isinstance(target, tf_decorator.TFDecorator))
