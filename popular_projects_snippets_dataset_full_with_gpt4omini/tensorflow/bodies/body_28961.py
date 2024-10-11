# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py
def generator():
    exit("foo")
    exit(b"bar")
    exit(u"baz")

dataset = dataset_ops.Dataset.from_generator(
    generator, output_types=dtypes.string, output_shapes=[])
self.assertDatasetProduces(
    dataset, expected_output=[b"foo", b"bar", b"baz"])
