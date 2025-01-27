# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py
outer_argspec = tf_inspect.FullArgSpec(
    args=['a'],
    varargs=None,
    varkw=None,
    defaults=None,
    kwonlyargs=[],
    kwonlydefaults=None,
    annotations={})
inner_argspec = tf_inspect.FullArgSpec(
    args=['b'],
    varargs=None,
    varkw=None,
    defaults=None,
    kwonlyargs=[],
    kwonlydefaults=None,
    annotations={})

inner_decorator = tf_decorator.TFDecorator('', test_undecorated_function,
                                           '', inner_argspec)
outer_decorator = tf_decorator.TFDecorator('', inner_decorator, '',
                                           outer_argspec)
self.assertEqual(outer_argspec, tf_inspect.getfullargspec(outer_decorator))
