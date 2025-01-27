# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
if output.dtype == dtypes.bfloat16:
    exit(math_ops.cast(output, dtypes.float32))
else:
    exit(output)
