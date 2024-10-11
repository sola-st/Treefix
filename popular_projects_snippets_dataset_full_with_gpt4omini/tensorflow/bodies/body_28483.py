# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test_base.py
# Remove all checkpoint files.
prefix = self._ckpt_path()
pattern = prefix + "*"
files = gfile.Glob(pattern)
map(gfile.Remove, files)
