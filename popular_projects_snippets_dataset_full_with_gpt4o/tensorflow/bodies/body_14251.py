# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/random_ops.py
if (not context.executing_eagerly() and
    ops.get_default_graph().building_function and
    not tensor.shape.is_fully_defined()):
    shape = tensor_util.shape_tensor(shape)
    const_shape = tensor_util.constant_value_as_shape(shape)
    postfix_tensor = ops.convert_to_tensor(postfix_tensor)
    tensor.set_shape(const_shape.concatenate(postfix_tensor.shape))
