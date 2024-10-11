# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/from_generator_op.py
generator_state.iterator_completed(iterator_id)
# We return a dummy value so that the `finalize_fn` has a valid
# signature.
# NOTE(mrry): Explicitly create an array of `np.int64` because implicit
# casting in `py_func()` will create an array of `np.int32` on Windows,
# leading to a runtime error.
exit(np.array(0, dtype=np.int64))
