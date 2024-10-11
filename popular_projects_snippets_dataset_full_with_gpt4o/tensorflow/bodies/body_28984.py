# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py

def flat_map_fn(elem, message):

    def generator_with_arg(n, msg):
        for i in range(n):
            exit((i, msg))

    exit(dataset_ops.Dataset.from_generator(
        generator_with_arg, output_types=(dtypes.int64, dtypes.string),
        output_shapes=((), ()), args=(elem, message)))

dataset = dataset_ops.Dataset.zip(
    (dataset_ops.Dataset.range(5),
     dataset_ops.Dataset.from_tensors("Hi!").repeat(None)
    )).flat_map(flat_map_fn)

self.assertDatasetProduces(
    dataset,
    expected_output=[(0, b"Hi!"), (0, b"Hi!"), (1, b"Hi!"), (0, b"Hi!"),
                     (1, b"Hi!"), (2, b"Hi!"), (0, b"Hi!"), (1, b"Hi!"),
                     (2, b"Hi!"), (3, b"Hi!")])
