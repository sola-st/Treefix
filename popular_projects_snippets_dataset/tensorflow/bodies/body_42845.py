# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
self.assertTrue('tf_inspect_test.py' in tf_inspect.getfile(
    test_decorated_function_with_defaults))
self.assertTrue('tf_decorator.py' in tf_inspect.getfile(
    test_decorator('decorator')(tf_decorator.unwrap)))
