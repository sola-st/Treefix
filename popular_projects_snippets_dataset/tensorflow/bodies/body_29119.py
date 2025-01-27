# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/unbatch_test.py
data = tuple([(math_ops.range(10 * i, 10 * i + 10),
               array_ops.fill([10], "hi")) for i in range(3)])
data = dataset_ops.Dataset.from_tensor_slices(data)
expected_types = ((dtypes.int32, dtypes.string),) * 3
data = data.batch(2)
self.assertAllEqual(expected_types,
                    dataset_ops.get_legacy_output_types(data))
data = data.unbatch()
self.assertAllEqual(expected_types,
                    dataset_ops.get_legacy_output_types(data))

self.assertDatasetProduces(
    data,
    [((i, b"hi"), (10 + i, b"hi"), (20 + i, b"hi")) for i in range(10)])
