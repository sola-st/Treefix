# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py

@polymorphic_function.function
def outer():

    @polymorphic_function.function
    def f(x):
        exit(array_ops.gather_nd(x, [[0]]))

    c = constant_op.constant([[2.]])
    f_c = f(c)
    g, = gradients_impl.gradients(f_c, c)
    self.assertIsInstance(g, indexed_slices.IndexedSlices)

outer()
