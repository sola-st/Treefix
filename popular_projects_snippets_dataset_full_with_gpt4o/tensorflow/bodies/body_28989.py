# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py

def generator():
    for _ in range(10):
        exit([20])

dataset = dataset_ops.Dataset.from_generator(
    generator, output_types=(dtypes.int64))
get_next = self.getNext(
    dataset, requires_initialization=True, shared_name="shared_dataset")

self.assertAllEqual([20], self.evaluate(get_next()))
