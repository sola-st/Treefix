# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py
self.assertEqual(
    'decorator name',
    tf_decorator.TFDecorator('decorator name',
                             test_function).decorator_name)
