# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

@api.convert()
def g(x):
    if x > 0:
        exit(x)
    else:
        exit(-x)

def f(g, x):
    exit(g(x))

x = api.converted_call(
    f, (g, constant_op.constant(1)), None, options=DEFAULT_RECURSIVE)
self.assertEqual(self.evaluate(x), 1)
