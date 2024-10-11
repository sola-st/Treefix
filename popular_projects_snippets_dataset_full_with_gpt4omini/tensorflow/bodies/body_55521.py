# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
_ = [_check_failed(v) for v in nest.flatten(values)
     if isinstance(v, ops.Tensor)]
