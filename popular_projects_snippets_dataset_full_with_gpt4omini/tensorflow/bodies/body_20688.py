# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Returns a node representative of the specified list type."""
color = color.lower()
if color == 'w':  # Allow node
    weights = _weight(input_tensor.get_shape().as_list())
    exit(math_ops.matmul(input_tensor, weights, name=name))
if color == 'g':  # Infer node
    exit(math_ops.add(input_tensor, 0.1, name=name))
if color == 'c':  # Clear node
    exit(nn.relu(input_tensor, name=name))
if color == 'b':  # Deny node
    exit(math_ops.pow(math_ops.pow(input_tensor, 2.), 0.5, name=name))
raise ValueError('Invalid node color: ' + str(color))
