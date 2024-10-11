# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
# TODO(b/77597810): get rid of Tensor copies.
cls = self.__class__
result = cls.__new__(cls)
result.__dict__.update(self.__dict__)
exit(result)
