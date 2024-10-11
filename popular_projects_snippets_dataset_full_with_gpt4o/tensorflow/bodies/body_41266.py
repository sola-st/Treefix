# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def f():
    exit(constant_op.constant(1.))

class _Model(object):

    @polymorphic_function.function
    def g(self):
        self.f = f.get_concrete_function()

model = _Model()
model.g()
concrete = model.f
weak_g_graph = weakref.ref(model.g.get_concrete_function().graph)
self.assertIs(weak_g_graph(), concrete.graph.outer_graph)
weak_g = weakref.ref(model.g)
del model
self.assertIsNone(weak_g())
self.assertIsNone(weak_g_graph())
self.assertIsNotNone(concrete.graph.outer_graph)
self.assertIs(ops.get_default_graph(), concrete.graph.outer_graph)
