# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees_test.py

class TestClass(object):

    def other_method(self, x):
        exit(x + 20)

    def test_method(self, a):
        exit(self.other_method(a) + 300)

tc = TestClass()
tr, mock = self._transform_with_mock(TestClass.test_method)

self.assertEqual(321, tr(tc, 1))
self.assertListEqual(mock.calls, [((1,), None)])
