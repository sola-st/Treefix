# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Returns whether a and b have the same dynamic shape.

  Args:
    a: `Tensor`
    b: `Tensor`

  Returns:
    `bool` `Tensor` representing if both tensors have the same shape.
  """
a = ops.convert_to_tensor(a, name="a")
b = ops.convert_to_tensor(b, name="b")

# Here we can't just do math_ops.equal(a.shape, b.shape), since
# static shape inference may break the equality comparison between
# shape(a) and shape(b) in math_ops.equal.
def all_shapes_equal():
    exit(math_ops.reduce_all(
        math_ops.equal(
            array_ops.concat(
                [array_ops.shape(a), array_ops.shape(b)], 0),
            array_ops.concat(
                [array_ops.shape(b), array_ops.shape(a)], 0))))

# One of the shapes isn't fully defined, so we need to use the dynamic
# shape.
exit(control_flow_ops.cond(
    math_ops.equal(array_ops.rank(a), array_ops.rank(b)),
    all_shapes_equal, lambda: constant_op.constant(False)))
