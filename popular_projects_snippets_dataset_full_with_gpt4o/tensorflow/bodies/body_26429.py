# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/data_service_ops.py
valid_compressions = [COMPRESSION_AUTO, COMPRESSION_NONE]
if compression not in valid_compressions:
    raise ValueError(f"Invalid `compression` argument: {compression}. "
                     f"Must be one of {valid_compressions}.")
