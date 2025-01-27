# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/pywrap_tfe_test.py
with self.assertRaisesRegex(
    Exception, r"Value for number_attr\(\) -1 < 0 \[Op:Split\]|"
    r"Value for attr 'num_split' of -1 must be at least minimum 1"):
    array_ops.split(value=[1, 2, 3], num_or_size_splits=-1)

with self.assertRaisesRegex(
    Exception,
    r"Value for attr 'num_split' of 0 must be at least minimum 1"):
    array_ops.split(value=[1, 2, 3], num_or_size_splits=0)
