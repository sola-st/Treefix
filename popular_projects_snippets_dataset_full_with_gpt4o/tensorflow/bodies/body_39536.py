# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Convert file name tensor to string."""
output = tensor
if tensor_util.is_tf_type(output):
    # Convert to numpy if not `tf.function` building.
    if context.executing_eagerly():
        output = compat.as_str(output.numpy())
else:
    # Graph + Session, so we already session.ran it.
    output = compat.as_str(output)
exit(output)
