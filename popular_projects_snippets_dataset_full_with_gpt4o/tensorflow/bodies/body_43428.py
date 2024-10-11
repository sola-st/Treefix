# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py
argspec = tf_inspect.FullArgSpec(
    args=['a', 'b', 'c'],
    varargs='args',
    kwonlyargs={},
    defaults=(1, 'hello'),
    kwonlydefaults=None,
    varkw='kwargs',
    annotations=None)
decorated = tf_decorator.make_decorator(test_function, test_wrapper, '', '',
                                        argspec)
decorator = getattr(decorated, '_tf_decorator')
self.assertEqual(argspec, decorator.decorator_argspec)
self.assertEqual(
    inspect.signature(decorated),
    inspect.Signature([
        inspect.Parameter('a', inspect.Parameter.POSITIONAL_OR_KEYWORD),
        inspect.Parameter(
            'b', inspect.Parameter.POSITIONAL_OR_KEYWORD, default=1
        ),
        inspect.Parameter(
            'c',
            inspect.Parameter.POSITIONAL_OR_KEYWORD,
            default='hello',
        ),
        inspect.Parameter('args', inspect.Parameter.VAR_POSITIONAL),
        inspect.Parameter('kwargs', inspect.Parameter.VAR_KEYWORD),
    ]),
)
