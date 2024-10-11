# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py
test_decorated_class = TestDecoratedClass()
self.assertEqual([2, 2, 3], test_decorated_class.return_params(1, 2, 3))
decorators, target = tf_decorator.unwrap(test_decorated_class.return_params)
self.assertEqual('test_decorator_increment_first_int_arg',
                 decorators[0].decorator_name)
self.assertEqual([1, 2, 3], target(test_decorated_class, 1, 2, 3))
