# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/io_ops_test.py
cases = ['', 'Some contents']
for contents in cases:
    contents = compat.as_bytes(contents)
    subdir = os.path.join(self.get_temp_dir(), 'subdir1')
    filepath = os.path.join(subdir, 'subdir2', 'filename')
    with self.cached_session() as sess:
        w = io_ops.write_file(filepath, contents)
        self.evaluate(w)
        with open(filepath, 'rb') as f:
            file_contents = f.read()
        self.assertEqual(file_contents, contents)
    shutil.rmtree(subdir)
