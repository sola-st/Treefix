# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
signature = tf_inspect.signature(test_decorated_function_with_defaults)

self.assertEqual([
    tf_inspect.Parameter('a', tf_inspect.Parameter.POSITIONAL_OR_KEYWORD),
    tf_inspect.Parameter(
        'b', tf_inspect.Parameter.POSITIONAL_OR_KEYWORD, default=2),
    tf_inspect.Parameter(
        'c', tf_inspect.Parameter.POSITIONAL_OR_KEYWORD, default='Hello')
], list(signature.parameters.values()))
