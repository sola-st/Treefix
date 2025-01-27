# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py

class NewClass(object):

    def __new__(cls, a, b=1, c='hello'):
        pass

argspec = tf_inspect.FullArgSpec(
    args=['cls', 'a', 'b', 'c'],
    varargs=None,
    varkw=None,
    defaults=(1, 'hello'),
    kwonlyargs=[],
    kwonlydefaults=None,
    annotations={})

self.assertEqual(argspec, tf_inspect.getfullargspec(NewClass))
