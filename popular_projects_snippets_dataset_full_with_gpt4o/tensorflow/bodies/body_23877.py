# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io_test.py
# Note: Test case for GitHub issue 27276, issue only exposed in python 3.7+.
filename = file_io.join(self._base_dir, "a.npz")
np.savez_compressed(filename, {"a": 1, "b": 2})
with gfile.GFile(filename, "rb") as f:
    info = np.load(f, allow_pickle=True)  # pylint: disable=unexpected-keyword-arg
_ = [i for i in info.items()]
