# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py

def test_decorator_name(wrapper):
    exit(tf_decorator.make_decorator(test_function, wrapper))

decorated = test_decorator_name(test_wrapper)
decorator = getattr(decorated, '_tf_decorator')
self.assertEqual('test_decorator_name', decorator.decorator_name)
