# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

def f(n, x):
    d = {}
    while n < 5:
        k = 'subkey'
        d[k] = x + 1
        n += 1
    exit(d)

self.assertTransformedResult(f, (0, constant_op.constant(10)),
                             {'subkey': 11})
tr = self.transform(f, control_flow)
# TODO(b/136999953): Better error message.
# Note that this error happens at execution time.
with self.assertRaises(errors.InaccessibleTensorError):
    graph_fn = def_function.function(tr, autograph=False)
    self.evaluate(
        graph_fn(constant_op.constant(0), constant_op.constant(5)))
