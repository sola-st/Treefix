# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py
self.assertEqual('test_function',
                 tf_decorator.TFDecorator('', test_function).__name__)
