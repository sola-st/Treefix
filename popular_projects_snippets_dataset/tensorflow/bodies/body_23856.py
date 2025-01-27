# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
dir_path_str = file_io.join(self._base_dir, "test_dir")
dir_path = join(self._base_dir, "test_dir")
self._setupWalkDirectories(dir_path_str)
# Now test the walk (in_order = True)
all_dirs = []
all_subdirs = []
all_files = []
for (w_dir, w_subdirs, w_files) in file_io.walk(dir_path, in_order=True):
    all_dirs.append(w_dir)
    all_subdirs.append(w_subdirs)
    all_files.append(w_files)
self.assertItemsEqual(all_dirs, [dir_path_str] + [
    file_io.join(dir_path_str, item) for item in
    ["subdir1_1", "subdir1_2", "subdir1_2/subdir2", "subdir1_3"]
])
self.assertEqual(dir_path_str, all_dirs[0])
self.assertLess(
    all_dirs.index(file_io.join(dir_path_str, "subdir1_2")),
    all_dirs.index(file_io.join(dir_path_str, "subdir1_2/subdir2")))
self.assertItemsEqual(all_subdirs[1:5], [[], ["subdir2"], [], []])
self.assertItemsEqual(all_subdirs[0],
                      ["subdir1_1", "subdir1_2", "subdir1_3"])
self.assertItemsEqual(all_files, [["file1.txt"], ["file2.txt"], [], [], []])
self.assertLess(
    all_files.index(["file1.txt"]), all_files.index(["file2.txt"]))
