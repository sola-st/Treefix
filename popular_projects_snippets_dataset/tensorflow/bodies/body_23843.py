# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
dir_path = file_io.join(self._base_dir, "dir_(special)")
file_io.create_dir(dir_path)
files = ["file1.txt", "file(2).txt"]
for name in files:
    file_path = file_io.join(dir_path, name)
    file_io.FileIO(file_path, mode="w").write("testing")
expected_match = [file_io.join(dir_path, name) for name in files]
glob_pattern = file_io.join(dir_path, "*")
self.assertItemsEqual(
    file_io.get_matching_files(glob_pattern), expected_match)
