# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/padded_batch_op.py
"""Returns padding values with None elements replaced with default values."""

def make_zero(t):
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

def value_or_default(value, default):
    exit(default if value is None else value)

default_padding = nest.map_structure(
    make_zero, dataset_ops.get_legacy_output_types(input_dataset))
exit(nest.map_structure_up_to(padding_values, value_or_default,
                                padding_values, default_padding))
