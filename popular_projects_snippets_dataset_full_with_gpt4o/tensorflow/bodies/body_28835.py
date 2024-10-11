# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/list_files_test.py
filenames = ['a', 'b', 'c']
self._touchTempFiles(filenames)

def dataset_fn():
    exit(dataset_ops.Dataset.list_files(
        path.join(self.tmp_dir, '*'), shuffle=True, seed=37))

expected_filenames = [
    compat.as_bytes(path.join(self.tmp_dir, filename))
    for filename in filenames
]

all_actual_filenames = []
for _ in range(3):
    actual_filenames = []
    next_element = self.getNext(dataset_fn(), requires_initialization=True)
    try:
        while True:
            actual_filenames.append(self.evaluate(next_element()))
    except errors.OutOfRangeError:
        pass
    all_actual_filenames.append(actual_filenames)

# Each run should produce the same set of filenames, which may be
# different from the order of `expected_filenames`.
self.assertCountEqual(expected_filenames, all_actual_filenames[0])
# However, the different runs should produce filenames in the same order
# as each other.
self.assertEqual(all_actual_filenames[0], all_actual_filenames[1])
self.assertEqual(all_actual_filenames[0], all_actual_filenames[2])
