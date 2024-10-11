# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_tf_record_dataset_test.py

def dataset_fn():
    exit(readers.make_tf_record_dataset(
        file_pattern=self._filenames,
        num_epochs=num_epochs,
        batch_size=batch_size,
        num_parallel_reads=num_parallel_reads,
        shuffle=True,
        shuffle_seed=seed))

next_element = self.getNext(dataset_fn())
first_batches = []
try:
    while True:
        first_batches.append(self.evaluate(next_element()))
except errors.OutOfRangeError:
    pass

next_element = self.getNext(dataset_fn())
second_batches = []
try:
    while True:
        second_batches.append(self.evaluate(next_element()))
except errors.OutOfRangeError:
    pass

self.assertEqual(len(first_batches), len(second_batches))
if seed is not None:
    # if you set a seed, should get the same results
    for i in range(len(first_batches)):
        self.assertAllEqual(first_batches[i], second_batches[i])

expected = []
for f in range(self._num_files):
    for r in range(self._num_records):
        expected.extend([self._record(f, r)] * num_epochs)

for batches in (first_batches, second_batches):
    actual = []
    for b in batches:
        actual.extend(b)
    self.assertAllEqual(sorted(expected), sorted(actual))
