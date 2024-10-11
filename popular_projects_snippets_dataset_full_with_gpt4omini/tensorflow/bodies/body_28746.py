# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
# Non-matching structure for types and shapes.
with self.assertRaises(TypeError):
    iterator = iterator_ops.Iterator.from_structure(
        (dtypes.int64, dtypes.float64), [None])

# Test validation of dataset argument.
iterator = iterator_ops.Iterator.from_structure((dtypes.int64,
                                                 dtypes.float64))

# Incompatible structure.
with self.assertRaisesRegex(
    ValueError, "The two structures don't have the same nested structure."):
    iterator.make_initializer(
        dataset_ops.Dataset.from_tensors(((constant_op.constant(
            [1, 2, 3], dtype=dtypes.int64),), (constant_op.constant(
                [4., 5., 6., 7.], dtype=dtypes.float64),))))

# Incompatible types.
with self.assertRaisesRegex(
    TypeError,
    r"Expected output types \(tf.int64, tf.float64\) but got dataset with "
    r"output types \(tf.int32, tf.float32\)."):
    iterator.make_initializer(
        dataset_ops.Dataset.from_tensors(
            (constant_op.constant([1, 2, 3], dtype=dtypes.int32),
             constant_op.constant([4., 5., 6., 7.], dtype=dtypes.float32))))

# Incompatible shapes.
iterator = iterator_ops.Iterator.from_structure(
    (dtypes.int64, dtypes.float64), ([None], []))
with self.assertRaisesRegex(
    TypeError,
    r"Expected output shapes compatible with .* but got dataset with "
    r"output shapes.*"):
    iterator.make_initializer(
        dataset_ops.Dataset.from_tensors(
            (constant_op.constant([1, 2, 3], dtype=dtypes.int64),
             constant_op.constant([4., 5., 6., 7.], dtype=dtypes.float64))))
