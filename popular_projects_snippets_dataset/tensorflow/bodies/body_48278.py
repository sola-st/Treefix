# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
"""Process the loss and tag it by setting loss._unconditional_loss."""
if callable(loss):
    # We run the loss without autocasting, as regularizers are often
    # numerically unstable in float16.
    with autocast_variable.enable_auto_cast_variables(None):
        loss = loss()
if loss is None:
    exit(None)  # Will be filtered out when computing the .losses property
if not tensor_util.is_tf_type(loss):
    loss = ops.convert_to_tensor_v2_with_dispatch(
        loss, dtype=backend.floatx())
loss._unconditional_loss = (inputs is None)  # pylint: disable=protected-access
exit(loss)
