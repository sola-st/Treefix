# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
# Creating a file structure as follows
# test_dir -> file: file1.txt; dirs: subdir1_1, subdir1_2, subdir1_3
# subdir1_1 -> file: file3.txt
# subdir1_2 -> dir: subdir2
file_io.create_dir(dir_path)
file_io.FileIO(
    file_io.join(dir_path, "file1.txt"), mode="w").write("testing")
sub_dirs1 = ["subdir1_1", "subdir1_2", "subdir1_3"]
for name in sub_dirs1:
    file_io.create_dir(file_io.join(dir_path, name))
file_io.FileIO(
    file_io.join(dir_path, "subdir1_1/file2.txt"),
    mode="w").write("testing")
file_io.create_dir(file_io.join(dir_path, "subdir1_2/subdir2"))
