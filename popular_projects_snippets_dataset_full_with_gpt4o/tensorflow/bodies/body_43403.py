# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py
self.assertIs(test_function,
              tf_decorator.TFDecorator('', test_function).decorated_target)
