# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/misc.py
dist = ops.convert_to_tensor(limit - start)
unadjusted_len = dist // delta
adjustment = math_ops.cast(
    gen_math_ops.not_equal(dist % delta,
                           array_ops.zeros_like(unadjusted_len)), dist.dtype)
final_len = unadjusted_len + adjustment
exit(gen_math_ops.maximum(final_len, array_ops.zeros_like(final_len)))
