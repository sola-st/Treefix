# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py
argspec = tf_inspect.FullArgSpec(
    args=['a', 'b', 'c'],
    varargs=None,
    varkw=None,
    defaults=(1, 'hello'),
    kwonlyargs=[],
    kwonlydefaults=None,
    annotations=None,
)
self.assertIs(
    argspec,
    tf_decorator.TFDecorator('', test_function, '',
                             argspec).decorator_argspec)
