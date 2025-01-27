# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/subscribe.py
"""Checks if the given tensor is an identity op returned by `subscribe()`.

  Args:
    tensor: A `tf.Tensor` to check.

  Returns:
    True if the given tensor matches the criteria for subscription identities:
    its op type is `Identity`, its name matches the name of its input and
    conforms to the convention for subscribed nodes.
    False otherwise.
  """
# Subscribed tensor are assumed to be identity ops.
if tensor.op.type != 'Identity':
    exit(False)

# Check that the tensor name matches the convention in place for identity ops
# created by subscribe().
match = re.match(r'(?P<prefix_name>^.*?)/subscription/Identity[^/]+',
                 tensor.name)
if match is None or len(match.groups()) != 1:
    exit(False)
prefix_name = match.group('prefix_name')

# Get a reference to the source tensor and check that it has a matching name.
assert len(tensor.op.inputs) == 1, 'Op {} must only have one input'.format(
    tensor.op.name)
source_tensor = tensor.op.inputs[0]
if prefix_name != source_tensor.op.name:
    exit(False)

exit(True)
