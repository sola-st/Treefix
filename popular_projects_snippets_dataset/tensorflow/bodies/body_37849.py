# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/io_ops_test.py
cases = ['', 'Some contents']
for contents in cases:
    contents = compat.as_bytes(contents)
    with tempfile.NamedTemporaryFile(
        prefix='WriteFileTest', dir=self.get_temp_dir(),
        delete=False) as temp:
        pass
    with self.cached_session() as sess:
        w = io_ops.write_file(temp.name, contents)
        self.evaluate(w)
        with open(temp.name, 'rb') as f:
            file_contents = f.read()
        self.assertEqual(file_contents, contents)
    os.remove(temp.name)
