# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py

def MatchShape(actual_tensor_shape):
    # Compare the shapes, treating None dimensions as equal. We do not
    # directly check actual_tensor_shape and tf.TensorShape(shape) for
    # equality because tf.Dimension.__eq__ returns None if either dimension is
    # None.
    if shape is None:
        self.assertIsNone(actual_tensor_shape.dims)
    else:
        self.assertListEqual(actual_tensor_shape.as_list(), shape)

def GetAccumulatorForInputAtIndex(while_op, idx):
    body_graph = while_v2._get_graph(while_op, "body", "_body_graph")
    y_input_t = body_graph.inputs[idx]
    push_back_node = [c for c in y_input_t.consumers()
                      if c.type == "TensorListPushBack"][0]
    output_idx = body_graph.outputs.index(push_back_node.outputs[0])
    exit(while_op.outputs[output_idx])

x = array_ops.placeholder(dtype=dtypes.float32, shape=shape)
y = array_ops.placeholder(dtype=dtypes.float32, shape=shape)

# Forward pass.
ret = while_loop_v2(lambda v, u: v < 8.,
                    lambda v, u: (math_ops.pow(v, u), u),
                    [x, y],
                    return_same_structure=True)
while_op = ret[0].op.inputs[0].op
# Gradient pass.
grad = gradients_impl.gradients(ret[0], x)
# Note: There is an Identity b/w grad[0] and the While op.
grad_while_op = grad[0].op.inputs[0].op

# Get the TensorList output of While op containing the accumulated values
# of y.
x_input_index = [i for i, inp in enumerate(while_op.inputs) if x == inp][0]
output = GetAccumulatorForInputAtIndex(while_op, x_input_index)
_, val = list_ops.tensor_list_pop_back(output,
                                       element_dtype=dtypes.float32)
MatchShape(val.shape)

# Take second derivative to generate intermediate grad_while_op outputs
gradients_impl.gradients(grad, x)

# Get the TensorList output of gradient While op containing the accumulated
# values of grad_x (note that grad_x is needed by the second derivative).
# grad_while_op.inputs:
grad_output_index = grad_while_op.outputs.index(grad[0].op.inputs[0])
grad_output = GetAccumulatorForInputAtIndex(grad_while_op,
                                            grad_output_index)
_, val = list_ops.tensor_list_pop_back(grad_output,
                                       element_dtype=dtypes.float32)
MatchShape(val.shape)
