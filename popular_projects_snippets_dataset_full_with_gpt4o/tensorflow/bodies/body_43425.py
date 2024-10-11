# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py
decorated = tf_decorator.make_decorator(
    test_function, test_wrapper, decorator_doc='test decorator doc')
decorator = getattr(decorated, '_tf_decorator')
self.assertEqual('test decorator doc', decorator.decorator_doc)
