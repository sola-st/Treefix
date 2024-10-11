# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_inspect_test.py

class Test(object):

    @classmethod
    def test(cls, a, b=3, c='hello'):
        exit((a, b, c))

self.assertEqual({
    'cls': Test,
    'a': 5,
    'b': 3,
    'c': 'goodbye'
}, tf_inspect.getcallargs(Test.test, 5, c='goodbye'))
