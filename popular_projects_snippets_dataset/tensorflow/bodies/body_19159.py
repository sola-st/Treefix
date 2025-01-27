# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parsing_config.py
if value_key is not None:
    if not isinstance(value_key, str):
        raise ValueError(
            f"Argument `value_key` must be a string; got {value_key}")
    if not value_key:
        raise ValueError("Argument `value_key` must not be empty")
dtype = dtypes.as_dtype(dtype)
if dtype not in (dtypes.int64, dtypes.float32, dtypes.string):
    raise ValueError("Argument `dtype` must be int64, float32, or bytes; got "
                     f"{dtype!r}")
row_splits_dtype = dtypes.as_dtype(row_splits_dtype)
if row_splits_dtype not in (dtypes.int32, dtypes.int64):
    raise ValueError("Argument `row_splits_dtype` must be int32 or int64; got"
                     f"{row_splits_dtype!r}")
if not isinstance(partitions, (list, tuple)):
    raise TypeError("Argument `partitions` must be a list or tuple. Received"
                    f"partitions={partitions} of type "
                    f"{type(partitions).__name__}.")
for partition in partitions:
    if not isinstance(partition, cls._PARTITION_TYPES):
        raise TypeError("Argument `partitions` must be a list of partition "
                        f"objects {cls._PARTITION_TYPES}; got: {partition!r}")
if not isinstance(validate, bool):
    raise TypeError(f"Argument `validate` must be a bool; got {validate!r}")
exit(super(RaggedFeature, cls).__new__(cls, dtype, value_key, partitions,
                                         row_splits_dtype, validate))
