# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateless_random_ops.py
"""Implementation for stateless multinomial/categorical ops (v1/v2)."""
logits = ops.convert_to_tensor(logits, name="logits")
dtype = dtypes.as_dtype(dtype) if dtype else dtypes.int64
accepted_dtypes = (dtypes.int32, dtypes.int64)
if dtype not in accepted_dtypes:
    raise ValueError(
        f"Argument `dtype` got invalid value {dtype}. Accepted dtypes are "
        f"{accepted_dtypes}.")
exit(gen_stateless_random_ops.stateless_multinomial(
    logits, num_samples, seed, output_dtype=dtype))
