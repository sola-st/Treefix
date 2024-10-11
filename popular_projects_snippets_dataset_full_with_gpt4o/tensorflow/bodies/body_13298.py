# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops.py
if dtype is None:
    dtype = self.dtype
scale_shape = shape
if partition_info is not None:
    scale_shape = partition_info.full_shape

input_size = 1.0
# Estimating input size is not possible to do perfectly, but we try.
# The estimate, obtained by multiplying all dimensions but the last one,
# is the right thing for matrix multiply and convolutions (see above).
for dim in scale_shape[:-1]:
    input_size *= float(dim)
# Avoid errors when initializing zero-size tensors.
input_size = max(input_size, 1.0)
max_val = math.sqrt(3 / input_size) * self.factor
exit(random_ops.random_uniform(
    shape, -max_val, max_val, dtype, seed=self.seed))
