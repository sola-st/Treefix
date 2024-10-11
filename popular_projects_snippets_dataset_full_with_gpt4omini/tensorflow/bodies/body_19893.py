# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Checks all tensors in features to see if they are a direct input."""

# expand_composites here is important: as composite tensors pass through
# tpu.replicate, they get 'flattened' into their component tensors and then
# repacked before being passed to the tpu function. In means that it is the
# component tensors which are produced by an op with the
# "_tpu_input_identity" attribute.
for path, input_tensor in nest.flatten_with_joined_string_paths(
    features, expand_composites=True):
    if input_tensor.op.type == "Placeholder":
        continue
    try:
        is_input = input_tensor.op.get_attr("_tpu_input_identity")
    except ValueError:
        is_input = False
    if not is_input:
        raise ValueError(
            "Received input tensor {} which is the output of op {} (type {}) "
            "which does not have the `_tpu_input_identity` attr. Please "
            "ensure that the inputs to this layer are taken directly from "
            "the arguments of the function called by "
            "strategy.run. Two possible causes are: dynamic batch size "
            "support or you are using a keras layer and are not passing "
            "tensors which match the dtype of the `tf.keras.Input`s."
            "If you are triggering dynamic batch size support, you can "
            "disable it by passing tf.distribute.RunOptions("
            "experimental_enable_dynamic_batch_size=False) to the options "
            "argument of strategy.run().".format(path,
                                                 input_tensor.op.name,
                                                 input_tensor.op.type))
