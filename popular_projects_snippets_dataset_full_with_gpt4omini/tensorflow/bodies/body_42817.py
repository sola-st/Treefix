# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
"""Tests getargspec on partial function with decorated argspec."""

argspec = tf_inspect.FullArgSpec(
    args=['a', 'b', 'c'],
    varargs=None,
    varkw=None,
    defaults=(1, 'hello'),
    kwonlyargs=[],
    kwonlydefaults=None,
    annotations={},
)
decorator = tf_decorator.TFDecorator('', test_undecorated_function, '',
                                     argspec)
signature = inspect.Signature([
    inspect.Parameter(
        'a', inspect.Parameter.KEYWORD_ONLY, default=2
    ),
    inspect.Parameter(
        'b', inspect.Parameter.KEYWORD_ONLY, default=1
    ),
    inspect.Parameter(
        'c', inspect.Parameter.KEYWORD_ONLY, default='hello'
    ),
])
partial_with_decorator = functools.partial(decorator, a=2)
self.assertEqual(argspec, tf_inspect.getfullargspec(decorator))
self.assertEqual(signature, inspect.signature(partial_with_decorator))
