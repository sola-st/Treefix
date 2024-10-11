# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
file_path = file_io.join(self._base_dir, "temp_file")
with file_io.FileIO(file_path, mode="r+") as f:
    f.write("testing1\ntesting2\ntesting3\n\ntesting5")
with self.assertRaises(errors.InvalidArgumentError):
    # At present, this is sufficient to convince ourselves that the change
    # fixes the problem. That is, this test will seg fault without the change,
    # and pass with it. Unfortunately, this is brittle, as it relies on the
    # Python layer to pass the argument along to the wrapped C++ without
    # checking the argument itself.
    f.read(-2)
