# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
dir_path = file_io.join(self._base_dir, "temp_dir")
file_io.create_dir(dir_path)
files = ["file1.txt", "file2.txt", "file3.txt", "file*.txt"]
for name in files:
    file_path = file_io.join(dir_path, name)
    file_io.FileIO(file_path, mode="w").write("testing")
expected_match = [file_io.join(dir_path, name) for name in files]
self.assertItemsEqual(
    file_io.get_matching_files(file_io.join(dir_path, "file*.txt")),
    expected_match)
self.assertItemsEqual(file_io.get_matching_files(tuple()), [])
files_subset = [
    file_io.join(dir_path, files[0]),
    file_io.join(dir_path, files[2])
]
self.assertItemsEqual(
    file_io.get_matching_files(files_subset), files_subset)
file_io.delete_recursively(dir_path)
self.assertFalse(file_io.file_exists(file_io.join(dir_path, "file3.txt")))
