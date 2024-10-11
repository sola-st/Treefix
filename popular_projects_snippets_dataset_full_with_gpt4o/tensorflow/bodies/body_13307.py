# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops.py
if dtype is None:
    dtype = self.dtype
# Check the shape
if len(shape) < 3 or len(shape) > 5:
    raise ValueError("The tensor to initialize, specified by argument `shape`"
                     " must be at least three-dimensional and at most "
                     f"five-dimensional. Received shape={shape}")

if shape[-2] > shape[-1]:
    raise ValueError(f"In_filters, specified by shape[-2]={shape[-2]} cannot "
                     "be greater than out_filters, specified by "
                     f"shape[-1]={shape[-1]}.")

# Generate a random matrix
a = random_ops.random_normal([shape[-1], shape[-1]],
                             dtype=dtype,
                             seed=self.seed)
# Compute the qr factorization
q, r = gen_linalg_ops.qr(a, full_matrices=False)
# Make Q uniform
d = array_ops.diag_part(r)
q *= math_ops.sign(d)
q = q[:shape[-2], :]
q *= math_ops.cast(self.gain, dtype=dtype)
if len(shape) == 3:
    weight = array_ops.scatter_nd([[(shape[0] - 1) // 2]],
                                  array_ops.expand_dims(q, 0), shape)
elif len(shape) == 4:
    weight = array_ops.scatter_nd([[(shape[0] - 1) // 2,
                                    (shape[1] - 1) // 2]],
                                  array_ops.expand_dims(q, 0), shape)
else:
    weight = array_ops.scatter_nd([[(shape[0] - 1) // 2, (shape[1] - 1) // 2,
                                    (shape[2] - 1) // 2]],
                                  array_ops.expand_dims(q, 0), shape)
exit(weight)
