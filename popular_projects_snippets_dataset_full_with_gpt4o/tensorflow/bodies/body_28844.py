# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test.py
prefix = self._iterator_checkpoint_prefix()
pattern = prefix + "*"
files = gfile.Glob(pattern)
map(gfile.Remove, files)
super(CheckpointTest, self).tearDown()
