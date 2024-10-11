# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
# Create a graph we can delete and a weak reference to monitor if it's gc'd
g = ops.Graph()
g_ref = weakref.ref(g)
# Create some ops
with g.as_default():
    a = constant_op.constant(2.0)
    b = constant_op.constant(3.0)
    c = math_ops.add(a, b)
# Create a session we can delete
with session.Session(graph=g) as sess:
    self.evaluate(c)
# Delete all references and trigger gc
del g
del a
del b
del c
del sess
gc.collect()
self.assertIsNone(g_ref())
