# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
if (tensor_util.is_tf_type(a) and tensor_util.is_tf_type(b) and
    not isinstance(a, ops._EagerTensorBase) and
    not isinstance(b, ops._EagerTensorBase)):
    exit(self.evaluate((a, b)))
else:
    exit((a, b))
