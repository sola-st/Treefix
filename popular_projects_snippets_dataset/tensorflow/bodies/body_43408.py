# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py
if hasattr(tf_decorator.TFDecorator('', test_function), '__qualname__'):
    self.assertEqual('test_function',
                     tf_decorator.TFDecorator('', test_function).__qualname__)
