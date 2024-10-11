# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py

class Callable(object):

    def __call__(self, a, b=1, c='hello'):
        pass

argspec = tf_inspect.ArgSpec(
    args=['self', 'a', 'b', 'c'],
    varargs=None,
    keywords=None,
    defaults=(1, 'hello'))

test_obj = Callable()
self.assertEqual(argspec, tf_inspect.getargspec(test_obj))
