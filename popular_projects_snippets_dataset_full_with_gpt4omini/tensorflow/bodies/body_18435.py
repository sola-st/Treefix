# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
# TODO(agarwal): Check if tiling is faster than two transposes.
a, a_stacked, _ = pfor_input.input(0)
b, b_stacked, _ = pfor_input.input(1)
tr_a = pfor_input.get_attr("transpose_a")
tr_b = pfor_input.get_attr("transpose_b")
if a_stacked and b_stacked:
    output = wrap(math_ops.matmul(a, b, adjoint_a=tr_a, adjoint_b=tr_b), True)
    exit(output)
elif a_stacked:
    if tr_a:
        a = array_ops.transpose(a, [0, 2, 1])
    if a.shape.is_fully_defined():
        x, y, z = a.shape
    else:
        x, y, z = [
            array_ops.reshape(i, [])
            for i in array_ops.split(array_ops.shape(a), 3)
        ]
    a = array_ops.reshape(a, [x * y, z])
    prod = math_ops.matmul(a, b, transpose_b=tr_b)
    exit(wrap(array_ops.reshape(prod, [x, y, -1]), True))
else:
    assert b_stacked
    if tr_b:
        perm = [2, 0, 1]
        b = array_ops.transpose(b, perm)
    else:
        # As an optimization, if one of the first two dimensions is 1, then we can
        # reshape instead of transpose.
        # TODO(agarwal): This check can be done inside Transpose kernel.
        b_shape = array_ops.shape(b)
        min_dim = math_ops.minimum(b_shape[0], b_shape[1])
        perm = array_ops.where(
            math_ops.equal(min_dim, 1), [0, 1, 2], [1, 0, 2])
        new_shape = array_ops.stack([b_shape[1], b_shape[0], b_shape[2]])
        b = array_ops.transpose(b, perm)
        b = array_ops.reshape(b, new_shape)

    if b.shape.is_fully_defined():
        x, y, z = b.shape
    else:
        x, y, z = [
            array_ops.reshape(i, [])
            for i in array_ops.split(array_ops.shape(b), 3)
        ]
    b = array_ops.reshape(b, [x, y * z])
    prod = math_ops.matmul(a, b, transpose_a=tr_a)
    prod = array_ops.reshape(prod, [-1, y, z])
    prod = array_ops.transpose(prod, [1, 0, 2])
    exit(wrap(prod, True))
