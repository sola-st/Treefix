# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/list_files_test.py
filenames = ['a', 'b', 'c']
self._touchTempFiles(filenames)

# Repeat the list twice and ensure that the order is the same each time.
# NOTE(mrry): This depends on an implementation detail of `list_files()`,
# which is that the list of files is captured when the iterator is
# initialized. Otherwise, or if e.g. the iterator were initialized more than
# once, it's possible that the non-determinism of `tf.matching_files()`
# would cause this test to fail. However, it serves as a useful confirmation
# that the `shuffle=False` argument is working as intended.
# TODO(b/73959787): Provide some ordering guarantees so that this test is
# more meaningful.
dataset = dataset_ops.Dataset.list_files(
    path.join(self.tmp_dir, '*'), shuffle=False).repeat(2)
next_element = self.getNext(dataset)

expected_filenames = []
actual_filenames = []
for filename in filenames * 2:
    expected_filenames.append(
        compat.as_bytes(path.join(self.tmp_dir, filename)))
    actual_filenames.append(compat.as_bytes(self.evaluate(next_element())))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(next_element())
self.assertCountEqual(expected_filenames, actual_filenames)
self.assertEqual(actual_filenames[:len(filenames)],
                 actual_filenames[len(filenames):])
