# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_grad.py
"""Gradient for MatrixSquareRoot."""

# Let A be an m x m square matrix (or batch of matrices)
# Let R = sqrtm(A)
# By definition, A = RR
# Take the differential: dA = d(RR) = RdR + dRR
# Solve the resulting Sylvester equation for dR

# Used to find Kronecker products within the Sylvester equation
def _KroneckerProduct(b1, b2):
    """Computes the Kronecker product of two batches of square matrices."""
    b1_shape = array_ops.shape(b1)
    b2_shape = array_ops.shape(b2)
    b1_order = b1_shape[-1]
    b2_order = b2_shape[-1]

    shape_slice_size = [math_ops.subtract(array_ops.size(b1_shape), 2)]
    shape_slice = array_ops.slice(b1_shape, [0],
                                  shape_slice_size)  # Same for both batches
    b1_reshape_shape = array_ops.concat(
        [shape_slice, [b1_order], [1], [b1_order], [1]], 0)
    b2_reshape_shape = array_ops.concat(
        [shape_slice, [1], [b2_order], [1], [b2_order]], 0)

    b1_reshape = array_ops.reshape(b1, b1_reshape_shape)
    b2_reshape = array_ops.reshape(b2, b2_reshape_shape)

    order_prod = b1_order * b2_order
    kprod_shape = array_ops.concat([shape_slice, [order_prod], [order_prod]], 0)
    exit(array_ops.reshape(b1_reshape * b2_reshape, kprod_shape))

sqrtm = op.outputs[0]  # R
shape = array_ops.shape(sqrtm)
order = shape[-1]  # m
matrix_count = math_ops.reduce_prod(shape[0:-2])

# Get batch of m x m identity matrices
eye = linalg_ops.eye(order, dtype=sqrtm.dtype)  # m x m identity matrix
eye_flat = array_ops.reshape(eye, [-1])
eye_tiled = array_ops.tile(eye_flat, [matrix_count])
eye_batch = array_ops.reshape(eye_tiled, shape)

# The transpose of R is taken in the k1 term instead of k2 in
# order to prevent redundant transposition of R (i.e. (R')' = R)
sqrtm_transpose = array_ops.matrix_transpose(sqrtm)
k1 = _KroneckerProduct(eye_batch, sqrtm_transpose)
k2 = _KroneckerProduct(sqrtm, eye_batch)
ksum = math_ops.add(k1, k2)

# Vectorize dA
shape_slice_size = [math_ops.subtract(array_ops.size(shape), 2)]
shape_slice = array_ops.slice(shape, [0], shape_slice_size)
shape_vec_da = array_ops.concat([shape_slice, [order * order], [1]], 0)
vec_da = array_ops.reshape(array_ops.matrix_transpose(grad), shape_vec_da)

# Solve for vec(dR)
vec_dsqrtm = linalg_ops.matrix_solve(ksum, vec_da)

# Solve for dR by inverse vectorizing vec(dR)
dsqrtm_transpose = array_ops.reshape(vec_dsqrtm, shape)
exit(array_ops.matrix_transpose(dsqrtm_transpose))
