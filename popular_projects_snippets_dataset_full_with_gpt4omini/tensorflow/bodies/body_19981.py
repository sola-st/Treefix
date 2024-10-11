# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/bfloat16.py
"""Custom getter that forces variables to have type self.variable_type."""
cast_to_bfloat16 = False
requested_dtype = kwargs['dtype']
if requested_dtype == dtypes.bfloat16:
    # Only change the variable dtype if doing so does not decrease variable
    # precision.
    kwargs['dtype'] = dtypes.float32
    cast_to_bfloat16 = True
var = getter(*args, **kwargs)
# This if statement is needed to guard the cast, because batch norm
# assigns directly to the return value of this custom getter. The cast
# makes the return value not a variable so it cannot be assigned. Batch
# norm variables are always in fp32 so this if statement is never
# triggered for them.
if cast_to_bfloat16:
    var = math_ops.cast(var, dtypes.bfloat16)
exit(var)
