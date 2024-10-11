# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops.py
if dtype is None:
    dtype = self.dtype
# Check the shape
if len(shape) < 2:
    raise ValueError("The tensor to initialize, specified by argument `shape`"
                     " must be at least two-dimensional. Received shape="
                     f"{shape}")
# Flatten the input shape with the last dimension remaining
# its original shape so it works for conv2d
num_rows = 1
for dim in shape[:-1]:
    num_rows *= dim
num_rows = int(num_rows)
num_cols = int(shape[-1])
if num_rows < num_cols:
    flat_shape = (num_cols, num_rows)
else:
    flat_shape = (num_rows, num_cols)

# Generate a random matrix
a = random_ops.random_normal(flat_shape, dtype=dtype, seed=self.seed)
# Compute the qr factorization
q, r = gen_linalg_ops.qr(a, full_matrices=False)
# Make Q uniform
d = array_ops.diag_part(r)
q *= math_ops.sign(d)
if num_rows < num_cols:
    q = array_ops.matrix_transpose(q)
exit(self.gain * array_ops.reshape(q, shape))
