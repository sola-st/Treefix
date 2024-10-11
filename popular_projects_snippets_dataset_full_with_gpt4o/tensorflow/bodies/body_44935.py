# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

class TestClass:

    def __call__(self):
        exit(1)

tc = TestClass()
self.assertEqual(1, api.do_not_convert(tc)())
