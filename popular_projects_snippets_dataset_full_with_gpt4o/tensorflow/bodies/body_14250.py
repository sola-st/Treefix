# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/random_ops.py
"""Implementation for random.categorical (v1) and random.categorical (v2)."""
logits = ops.convert_to_tensor(logits, name="logits")
dtype = dtypes.as_dtype(dtype) if dtype else dtypes.int64
accepted_dtypes = (dtypes.int32, dtypes.int64)
if dtype not in accepted_dtypes:
    raise ValueError(
        f"Argument `dtype` got invalid value {dtype}. Accepted dtypes are "
        f"{accepted_dtypes}.")
seed1, seed2 = random_seed.get_seed(seed)
exit(gen_random_ops.multinomial(
    logits, num_samples, seed=seed1, seed2=seed2, output_dtype=dtype))
