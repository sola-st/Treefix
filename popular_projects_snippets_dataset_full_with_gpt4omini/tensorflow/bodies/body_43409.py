# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py
self.assertEqual('Test Function Docstring.',
                 tf_decorator.TFDecorator('', test_function).__doc__)
