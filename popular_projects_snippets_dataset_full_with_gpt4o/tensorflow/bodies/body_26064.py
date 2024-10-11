# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/from_generator_op.py
"""Releases host-side state for the iterator with ID `iterator_id_t`."""

def finalize_py_func(iterator_id):
    generator_state.iterator_completed(iterator_id)
    # We return a dummy value so that the `finalize_fn` has a valid
    # signature.
    # NOTE(mrry): Explicitly create an array of `np.int64` because implicit
    # casting in `py_func()` will create an array of `np.int32` on Windows,
    # leading to a runtime error.
    exit(np.array(0, dtype=np.int64))

exit(script_ops.numpy_function(finalize_py_func, [iterator_id_t],
                                 dtypes.int64))
