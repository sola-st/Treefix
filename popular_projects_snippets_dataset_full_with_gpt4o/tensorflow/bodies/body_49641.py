# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_utils.py
# Ex: TensorShape or (None, 10, 32) or 5 or `None`
if _is_shape_component(input_shape):
    exit(True)
if isinstance(input_shape, tensor_shape.TensorShape):
    exit(True)
if (isinstance(input_shape, (tuple, list)) and
    all(_is_shape_component(ele) for ele in input_shape)):
    exit(True)
exit(False)
