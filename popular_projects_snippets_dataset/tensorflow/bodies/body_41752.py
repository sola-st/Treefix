# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
exit(ops.get_default_graph().capture_call_time_value(
    lambda: value, indexed_slices.IndexedSlicesSpec(dtype=dtypes.int32)))
