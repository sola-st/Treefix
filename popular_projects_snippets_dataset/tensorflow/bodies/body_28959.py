# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py
def generator():
    exit([1])
    exit([2])
    exit([3])

for dtype in [dtypes.int8, dtypes.int32, dtypes.int64]:
    dataset = dataset_ops.Dataset.from_generator(
        generator, output_types=dtype, output_shapes=[1])
    get_next = self.getNext(dataset)

    for expected in [[1], [2], [3]]:
        next_val = self.evaluate(get_next())
        self.assertEqual(dtype.as_numpy_dtype, next_val.dtype)
        self.assertAllEqual(expected, next_val)
    with self.assertRaises(errors.OutOfRangeError):
        self.evaluate(get_next())
