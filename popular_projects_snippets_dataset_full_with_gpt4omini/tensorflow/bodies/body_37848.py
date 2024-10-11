# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/io_ops_test.py
cases = ['', 'Some contents', 'Неки садржаји на српском']
for contents in cases:
    contents = compat.as_bytes(contents)
    with tempfile.NamedTemporaryFile(
        prefix='ReadFileTest', dir=self.get_temp_dir(), delete=False) as temp:
        temp.write(contents)
    with self.cached_session():
        read = io_ops.read_file(temp.name)
        self.assertEqual([], read.get_shape())
        self.assertEqual(self.evaluate(read), contents)
    os.remove(temp.name)
