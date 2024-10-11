# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py
decorators, _ = tf_decorator.unwrap(test_decorated_function)
self.assertEqual('decorator 1', decorators[0].decorator_name)
self.assertEqual('test_decorator_increment_first_int_arg',
                 decorators[1].decorator_name)
self.assertEqual('decorator 3', decorators[2].decorator_name)
self.assertEqual('decorator 3 documentation', decorators[2].decorator_doc)
