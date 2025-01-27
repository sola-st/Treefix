# Extracted from ./data/repos/tensorflow/tensorflow/core/platform/ram_file_system_test.py
file_io.create_dir_v2('ram://testdirectory')
file_io.create_dir_v2('ram://testdirectory/subdir1')
file_io.create_dir_v2('ram://testdirectory/subdir2')
file_io.create_dir_v2('ram://testdirectory/subdir1/subdir3')
with gfile.GFile('ram://testdirectory/subdir1/subdir3/a.txt', 'w') as f:
    f.write('Hello, world.')
file_io.delete_recursively_v2('ram://testdirectory')
self.assertEqual(gfile.Glob('ram://testdirectory/*'), [])
