# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/io_ops_test.py
cases = [
    'ABcDEF.GH', 'ABzDEF.GH', 'ABasdfjklDEF.GH', 'AB3DEF.GH', 'AB4DEF.GH',
    'ABDEF.GH', 'XYZ'
]
files = [
    tempfile.NamedTemporaryFile(
        prefix=c, dir=self.get_temp_dir(), delete=True) for c in cases
]

with self.cached_session():
    # Test exact match without wildcards.
    for f in files:
        self.assertEqual(
            io_ops.matching_files(f.name).eval(), compat.as_bytes(f.name))

    # We will look for files matching "ABxDEF.GH*" where "x" is some wildcard.
    directory_path = files[0].name[:files[0].name.find(cases[0])]
    pattern = directory_path + 'AB%sDEF.GH*'

    self.assertEqual(
        set(io_ops.matching_files(pattern % 'z').eval()),
        self._subset(files, [1]))
    self.assertEqual(
        set(io_ops.matching_files(pattern % '?').eval()),
        self._subset(files, [0, 1, 3, 4]))
    self.assertEqual(
        set(io_ops.matching_files(pattern % '*').eval()),
        self._subset(files, [0, 1, 2, 3, 4, 5]))
    # NOTE(mrry): Windows uses PathMatchSpec to match file patterns, which
    # does not support the following expressions.
    if os.name != 'nt':
        self.assertEqual(
            set(io_ops.matching_files(pattern % '[cxz]').eval()),
            self._subset(files, [0, 1]))
        self.assertEqual(
            set(io_ops.matching_files(pattern % '[0-9]').eval()),
            self._subset(files, [3, 4]))

    # Test an empty list input.
    self.assertItemsEqual(io_ops.matching_files([]).eval(), [])

    # Test multiple exact filenames.
    self.assertItemsEqual(
        io_ops.matching_files([
            files[0].name, files[1].name, files[2].name]).eval(),
        self._subset(files, [0, 1, 2]))

    # Test multiple globs.
    self.assertItemsEqual(
        io_ops.matching_files([
            pattern % '?', directory_path + 'X?Z*']).eval(),
        self._subset(files, [0, 1, 3, 4, 6]))

for f in files:
    f.close()
