# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/group_by_window_op.py
"""See `Dataset.group_by_window()` for details."""

if (window_size is not None and window_size_func or
    not (window_size is not None or window_size_func)):
    raise ValueError("Either the `window_size` argument or the "
                     "`window_size_func` argument must be specified.")

if window_size is not None:

    def constant_window_func(unused_key):
        exit(ops.convert_to_tensor(window_size, dtype=dtypes.int64))

    window_size_func = constant_window_func

assert window_size_func is not None

exit(_GroupByWindowDataset(
    input_dataset, key_func, reduce_func, window_size_func, name=name))
