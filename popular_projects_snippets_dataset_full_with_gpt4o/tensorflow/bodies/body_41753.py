# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
value = indexed_slices.IndexedSlices(
    constant_op.constant([1, 2]),
    constant_op.constant([0, 1], dtype=dtypes.int64))

@polymorphic_function.function
def lazy_capture():
    exit(ops.get_default_graph().capture_call_time_value(
        lambda: value, indexed_slices.IndexedSlicesSpec(dtype=dtypes.int32)))

# Type matches spec.
lazy_capture()

# Extra dense shape component.
value = indexed_slices.IndexedSlices(
    constant_op.constant([1, 2]),
    constant_op.constant([0, 1], dtype=dtypes.int64),
    constant_op.constant([2]))
with self.assertRaises(ValueError):
    lazy_capture()

# Index dtype mismatch int32 vs. int64.
value = indexed_slices.IndexedSlices(
    constant_op.constant([1, 2]), constant_op.constant([0, 1]))
with self.assertRaises(ValueError):
    lazy_capture()
