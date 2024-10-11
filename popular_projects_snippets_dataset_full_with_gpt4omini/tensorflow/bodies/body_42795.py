# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
argspec = tf_inspect.FullArgSpec(
    args=['a', 'b', 'c'],
    varargs=None,
    varkw=None,
    defaults=(1, 'hello'),
    kwonlyargs=[],
    kwonlydefaults=None,
    annotations={},
)

inner_decorator = tf_decorator.TFDecorator('', test_undecorated_function,
                                           '', argspec)
outer_decorator = tf_decorator.TFDecorator('', inner_decorator)
self.assertEqual(argspec, tf_inspect.getargspec(outer_decorator))
