# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
split_dim = 1
value = [[0, 1, 2], [3, 4, 5]]
x1, x2, x3 = execute(
    b'Split',
    num_outputs=3,
    inputs=[constant_op.constant(split_dim),
            constant_op.constant(value)],
    attrs=('num_split', 3, 'T', dtypes.int32.as_datatype_enum))
self.assertAllEqual([[0], [3]], x1)
self.assertAllEqual([[1], [4]], x2)
self.assertAllEqual([[2], [5]], x3)
