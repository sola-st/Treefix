# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
table = self.getHashTable()(
    lookup_ops.KeyValueTensorInitializer(
        constant_op.constant([2, 5], dtype=dtypes.int64),
        constant_op.constant([-10.0, 1], dtype=dtypes.float32)),
    -1,
    experimental_is_anonymous=is_anonymous)
actual_shapes = [t.shape for t in table.export()]
inferred_shapes = []

@def_function.function
def f():
    for t in table.export():
        inferred_shapes.append(t.shape)

f()
self.assertLen(actual_shapes, 2)
self.assertLen(inferred_shapes, 2)
self.assertTrue(inferred_shapes[0].is_compatible_with(actual_shapes[0]))
self.assertTrue(inferred_shapes[1].is_compatible_with(actual_shapes[1]))
