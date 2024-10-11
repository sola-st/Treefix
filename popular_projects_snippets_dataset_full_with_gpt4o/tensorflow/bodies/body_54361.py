# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
# This device function unconditionally overwrites the device of ops.
#
# NOTE(mrry): Writing device functions like this is not
# recommended. Instead, in most cases you should use
# `pydev.merge_device("/job:ps")` or simply `"/job:ps"` as the
# argument to `tf.device()` and the device component will be merged in.
exit("/job:overwrite")
