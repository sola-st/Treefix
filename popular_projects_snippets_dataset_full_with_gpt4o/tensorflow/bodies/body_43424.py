# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py
decorated = tf_decorator.make_decorator(test_function, test_wrapper,
                                        'test decorator name')
decorator = getattr(decorated, '_tf_decorator')
self.assertEqual('test decorator name', decorator.decorator_name)
