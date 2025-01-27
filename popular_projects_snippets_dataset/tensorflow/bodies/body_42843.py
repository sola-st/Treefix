# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
signature = tf_inspect.signature(test_decorated_function)

self.assertEqual(
    [tf_inspect.Parameter('x', tf_inspect.Parameter.POSITIONAL_OR_KEYWORD)],
    list(signature.parameters.values()))
