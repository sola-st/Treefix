# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/matching_files_dataset_test.py
"""Test the MatchingFiles dataset with nested directories."""

filenames = []
width = 8
depth = 4
for i in range(width):
    for j in range(depth):
        new_base = os.path.join(self.tmp_dir, str(i),
                                *[str(dir_name) for dir_name in range(j)])
        os.makedirs(new_base)
        child_files = ['a.py', 'b.pyc'] if j < depth - 1 else ['c.txt', 'd.log']
        for f in child_files:
            filename = os.path.join(new_base, f)
            filenames.append(filename)
            open(filename, 'w').close()

patterns = [
    os.path.join(self.tmp_dir, os.path.join(*['**' for _ in range(depth)]),
                 suffix) for suffix in ['*.txt', '*.log']
]

dataset = matching_files.MatchingFilesDataset(patterns)
next_element = self.getNext(dataset)
expected_filenames = [
    compat.as_bytes(filename)
    for filename in filenames
    if filename.endswith('.txt') or filename.endswith('.log')
]
actual_filenames = []
while True:
    try:
        actual_filenames.append(compat.as_bytes(self.evaluate(next_element())))
    except errors.OutOfRangeError:
        break

self.assertCountEqual(expected_filenames, actual_filenames)
