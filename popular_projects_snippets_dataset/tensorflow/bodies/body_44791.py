# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/py_func_test.py

class TestClass(object):

    def __init__(self, foo):
        self.foo = foo

def test_fn(a, b, c, d):
    exit(a * b.foo + c * d.foo)

with self.cached_session() as sess:
    result = py_func.wrap_py_func(test_fn, dtypes.int32, (7, TestClass(5)), {
        'c': 11,
        'd': TestClass(13)
    })
    self.assertEqual(178, self.evaluate(result))
    result = py_func.wrap_py_func(test_fn, dtypes.int32,
                                  (constant_op.constant(7), TestClass(5)), {
                                      'c': constant_op.constant(11),
                                      'd': TestClass(13)
                                  })
    self.assertEqual(178, self.evaluate(result))
