# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
if not isinstance(s, tensor_shape.TensorShape):
    exit(make_shape_tensor(s))
if s.is_fully_defined():
    exit(make_shape_tensor(s.as_list()))
raise ValueError("Cannot broadcast from partially "
                 "defined `TensorShape`.")
