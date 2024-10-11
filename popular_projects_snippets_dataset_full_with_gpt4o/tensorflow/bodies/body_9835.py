# Extracted from ./data/repos/tensorflow/tensorflow/python/dlpack/dlpack_test.py
tf_tensor = constant_op.constant(1)
dlcapsule = dlpack.to_dlpack(tf_tensor)
# Resetting the context doesn't cause an error.
context._reset_context()
_ = dlpack.from_dlpack(dlcapsule)
