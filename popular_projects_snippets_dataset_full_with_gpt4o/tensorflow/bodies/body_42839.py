# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py

class InitClass(object):

    def __init__(self, a, b=1, c='hello'):
        pass

argspec = tf_inspect.FullArgSpec(
    args=['self', 'a', 'b', 'c'],
    varargs=None,
    varkw=None,
    defaults=(1, 'hello'),
    kwonlyargs=[],
    kwonlydefaults=None,
    annotations={})

self.assertEqual(argspec, tf_inspect.getfullargspec(InitClass))
