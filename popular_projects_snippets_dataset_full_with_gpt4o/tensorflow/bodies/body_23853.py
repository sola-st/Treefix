# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
dir_path = join(self._base_dir, "test_dir")
file_io.create_dir(dir_path)
files = ["file1.txt", "file2.txt", "file3.txt"]
for name in files:
    file_path = join(str(dir_path), name)
    file_io.FileIO(file_path, mode="w").write("testing")
subdir_path = join(str(dir_path), "sub_dir")
file_io.create_dir(subdir_path)
subdir_file_path = join(str(subdir_path), "file4.txt")
file_io.FileIO(subdir_file_path, mode="w").write("testing")
dir_list = file_io.list_directory(dir_path)
self.assertItemsEqual(files + ["sub_dir"], dir_list)
