# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with context.eager_mode():
    var = variables.Variable([[0.0], [0.0], [0.0], [0.0]], name="tensor")
    with backprop.GradientTape() as tape:
        a = array_ops.gather(array_ops.gather(var, [0, 1]), [0, 1])
        b = array_ops.gather(array_ops.gather(var, [2, 3]), [0, 1])
        r = special_math_ops.einsum("ij,ij->i", a, b)
    g = tape.gradient(r, [var])[0]
    values = g.values if isinstance(g, indexed_slices.IndexedSlices) else g
    self.assertAllEqual(values.get_shape(), [4, 1])
