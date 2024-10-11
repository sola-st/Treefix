# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
sizes = [1, 0, 2, 10]
sizes_iter = iter(sizes)
def gen():
    for i in range(next(sizes_iter)):
        exit(i)

dataset = dataset_ops.Dataset.from_generator(
    gen, output_signature=tensor_spec.TensorSpec((), dtypes.int64))
dataset = dataset.shuffle(10).repeat().take(3)
self.assertDatasetProduces(dataset, [0, 0, 1], assert_items_equal=True)
