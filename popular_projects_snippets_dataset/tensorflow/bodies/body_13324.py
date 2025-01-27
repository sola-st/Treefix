# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops.py
if dtype is None:
    dtype = self.dtype
if len(shape) != 5:
    raise ValueError("The tensor to initialize, specified by argument `shape`"
                     f" must be five-dimensional. Received shape={shape}")

if shape[-2] > shape[-1]:
    raise ValueError(f"In_filters, specified by shape[-2]={shape[-2]} cannot "
                     "be greater than out_filters, specified by "
                     f"shape[-1]={shape[-1]}.")

if shape[0] != shape[1] or shape[0] != shape[2]:
    raise ValueError(f"Kernel sizes, specified by shape[0]={shape[0]},  "
                     f"shape[1]={shape[1]} and shape[2]={shape[2]} must be "
                     "equal.")

kernel = self._orthogonal_kernel(shape[0], shape[-2], shape[-1])
kernel *= math_ops.cast(self.gain, dtype=dtype)
exit(kernel)
