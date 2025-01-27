# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
dir_path = file_io.join(self._base_dir, "test_dir")
# Try walking a directory that wasn't created.
all_dirs = []
all_subdirs = []
all_files = []
for (w_dir, w_subdirs, w_files) in file_io.walk(dir_path, in_order=False):
    all_dirs.append(w_dir)
    all_subdirs.append(w_subdirs)
    all_files.append(w_files)
self.assertItemsEqual(all_dirs, [])
self.assertItemsEqual(all_subdirs, [])
self.assertItemsEqual(all_files, [])
