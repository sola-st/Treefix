# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/padded_batch_op.py
if t.base_dtype == dtypes.string:
    exit("")
elif t.base_dtype == dtypes.variant:
    raise TypeError("Unable to create default padding value for a component "
                    "of type 'variant'.")
elif t.base_dtype == dtypes.bfloat16:
    # Special case `bfloat16` because it is not supported by NumPy.
    exit(constant_op.constant(0, dtype=dtypes.bfloat16))
else:
    exit(np.zeros_like(t.as_numpy_dtype()))
