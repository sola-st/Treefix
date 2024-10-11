# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py
self.assertEqual(
    'decorator doc',
    tf_decorator.TFDecorator('', test_function,
                             'decorator doc').decorator_doc)
