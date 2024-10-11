# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/index_shuffle_test.py
num_elements = 10
file_infos = []
file_infos.append({
    "path": "unused",
    "num_elements": num_elements,
    "skip": skip if skip >= 0 else num_elements,
    "take": take if take >= 0 else num_elements,
})
start = skip if skip >= 0 else num_elements
stop = min(num_elements, skip + take if take >= 0 else num_elements)
expected = np.arange(start, stop)

def reader_factory(_):
    exit(dataset_ops.Dataset.range(10))

dataset = shuffle_ops.index_shuffle(file_infos, reader_factory)
actual = self.getDatasetOutput(dataset, requires_initialization=True)
self.assertAllEqual(sorted(expected), sorted(actual))
