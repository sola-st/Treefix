# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

def test_fn():
    res = TestResource()

    def f(y):

        def inner_f():
            exit(res.x + y)

        exit(inner_f)

    api.converted_call(f, (1,), None, options=DEFAULT_RECURSIVE)()

self.assertNoMemoryLeaks(test_fn)
