# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py
decorators, _ = tf_decorator.unwrap(test_decorated_function)
self.assertEqual(3, len(decorators))
self.assertTrue(isinstance(decorators[0], tf_decorator.TFDecorator))
self.assertTrue(isinstance(decorators[1], tf_decorator.TFDecorator))
self.assertTrue(isinstance(decorators[2], tf_decorator.TFDecorator))
self.assertIsNot(decorators[0], decorators[1])
self.assertIsNot(decorators[1], decorators[2])
self.assertIsNot(decorators[2], decorators[0])
