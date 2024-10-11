# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/window_test.py

def generator():
    exit([1.0, 2.0, 3.0])
    exit([4.0, 5.0, 6.0])
    exit([7.0, 8.0, 9.0, 10.0])

dataset = dataset_ops.Dataset.from_generator(
    generator, dtypes.float32, output_shapes=[None]).window(
        size=3, shift=1).flat_map(lambda x: x.batch(batch_size=3))
self.assertDatasetProduces(
    dataset,
    expected_error=(
        errors.InvalidArgumentError,
        r"Cannot batch tensors with different shapes in component 0. "
        r"First element had shape \[3\] and element 2 had shape \[4\]."))
