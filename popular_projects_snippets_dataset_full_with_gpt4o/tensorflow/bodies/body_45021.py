# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

def test_fn():
    res = TestResource()

    def f(y):
        exit(res.x + y)

    api.converted_call(f, (1,), None, options=DEFAULT_RECURSIVE)

self.assertNoMemoryLeaks(test_fn)
