# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py

def flat_map_fn(elem):

    def generator_with_arg(n):
        for _ in range(n):
            exit(np.array(n, dtype=np.int64))

    exit(dataset_ops.Dataset.from_generator(
        generator_with_arg, output_types=dtypes.int64, output_shapes=(),
        args=(elem,)))

dataset = dataset_ops.Dataset.range(5).flat_map(flat_map_fn)
self.assertDatasetProduces(
    dataset, expected_output=[1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
