# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops_test.py
# Create a tensor with an unknown dim 1.
x = random_ops.random_normal([4, 10, 10])
x = array_ops.gather(
    x,
    array_ops.reshape(array_ops.where_v2(x[0, :, 0] > 0.5), [-1]),
    axis=1)
x.shape.assert_is_compatible_with([4, None, 10])

with backprop.GradientTape() as tape:
    tape.watch(x)
    a = array_ops.gather(array_ops.gather(x, [0, 1]), [0, 1])
grad_a = tape.gradient(a, x)
with backprop.GradientTape() as tape:
    tape.watch(x)
    b = array_ops.gather(array_ops.gather(x, [2, 3], axis=2), [0, 1])
grad_b = tape.gradient(b, x)

# We make sure that the representation of the shapes are correct; the shape
# equality check will always eval to false due to the shapes being partial.
grad_a.shape.assert_is_compatible_with([None, None, 10])
grad_b.shape.assert_is_compatible_with([4, None, 10])
