# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/group_by_window_test.py
components = np.random.randint(50, size=(200,)).astype(np.int64)

def reduce_func(key, window):
    # Apply two different kinds of padding to the input: tight
    # padding, and quantized (to a multiple of 10) padding.
    exit(dataset_ops.Dataset.zip((
        window.padded_batch(
            4, padded_shapes=tensor_shape.TensorShape([None])),
        window.padded_batch(
            4, padded_shapes=ops.convert_to_tensor([(key + 1) * 10])),
    )))

dataset = dataset_ops.Dataset.from_tensor_slices(components)
dataset = dataset.map(
    lambda x: array_ops.fill([math_ops.cast(x, dtypes.int32)], x))
# pylint: disable=g-long-lambda
dataset = dataset.group_by_window(
    key_func=lambda x: math_ops.cast(
        array_ops.shape(x)[0] // 10, dtypes.int64),
    reduce_func=reduce_func,
    window_size=4)

get_next = self.getNext(dataset)
counts = []
with self.assertRaises(errors.OutOfRangeError):
    while True:
        tight_result, multiple_of_10_result = self.evaluate(get_next())
        self.assertEqual(0, multiple_of_10_result.shape[1] % 10)
        self.assertAllEqual(tight_result,
                            multiple_of_10_result[:, :tight_result.shape[1]])
        counts.append(tight_result.shape[0])
self.assertEqual(len(components), sum(counts))
