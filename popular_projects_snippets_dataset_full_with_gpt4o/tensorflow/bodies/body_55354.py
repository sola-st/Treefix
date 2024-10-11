# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.int32, dtypes.float32)
def Foo(t, x):
    exit(x[t])

@function.Defun(dtypes.int64)
def Bar(x):
    exit(x)

# NOTE(mrry): All functions are currently considered stateless by the
# runtime, so we simulate a "stateful" function.
# TODO(b/70565970): Remove this hack when we are able to build stateful
# functions using the API.
# pylint: disable=protected-access
Foo._signature.is_stateful = True
Bar._signature.is_stateful = True
# pylint: enable=protected-access

result_1 = Foo(3, [1.0, 2.0, 3.0, 4.0])
result_2 = Bar(constant_op.constant(100, dtype=dtypes.int64))

with session.Session() as sess:
    self.assertEqual(4.0, self.evaluate(result_1))
    self.assertEqual(100, self.evaluate(result_2))
    self.assertEqual((4.0, 100), sess.run((result_1, result_2)))
