# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
dir_path = file_io.join(self._base_dir, "test_dir")
self._setupWalkDirectories(dir_path)
# Now test the walk (in_order = False)
all_dirs = []
all_subdirs = []
all_files = []
for (w_dir, w_subdirs, w_files) in file_io.walk(dir_path, in_order=False):
    all_dirs.append(w_dir)
    all_subdirs.append(w_subdirs)
    all_files.append(w_files)
self.assertItemsEqual(all_dirs, [
    file_io.join(dir_path, item) for item in
    ["subdir1_1", "subdir1_2/subdir2", "subdir1_2", "subdir1_3"]
] + [dir_path])
self.assertEqual(dir_path, all_dirs[4])
self.assertLess(
    all_dirs.index(file_io.join(dir_path, "subdir1_2/subdir2")),
    all_dirs.index(file_io.join(dir_path, "subdir1_2")))
self.assertItemsEqual(all_subdirs[0:4], [[], [], ["subdir2"], []])
self.assertItemsEqual(all_subdirs[4],
                      ["subdir1_1", "subdir1_2", "subdir1_3"])
self.assertItemsEqual(all_files, [["file2.txt"], [], [], [], ["file1.txt"]])
self.assertLess(
    all_files.index(["file2.txt"]), all_files.index(["file1.txt"]))
