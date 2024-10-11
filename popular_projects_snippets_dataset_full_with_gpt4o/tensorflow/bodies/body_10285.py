# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_test.py
# We compute the batch norm manually in this function because
# nn_impl.batch_normalization does not support float16 yet.
# TODO(reedwm): Add float16 support to nn_impl.batch_normalization.
inv = math_ops.rsqrt(var + epsilon) * scale
y = math_ops.cast(x, scale.dtype) * inv + (offset - mean * inv)
exit(math_ops.cast(y, x.dtype))
