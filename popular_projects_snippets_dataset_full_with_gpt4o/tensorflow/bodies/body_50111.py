# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saving_utils.py
"""Trace the model call to create a tf.function for exporting a Keras model.

  Args:
    model: A Keras model.
    input_signature: optional, a list of tf.TensorSpec objects specifying the
      inputs to the model.

  Returns:
    A tf.function wrapping the model's call function with input signatures set.

  Raises:
    ValueError: if input signature cannot be inferred from the model.
  """
if input_signature is None:
    if isinstance(model.call, def_function.Function):
        input_signature = model.call.input_signature

if input_signature is None:
    input_signature = model_input_signature(model)

if input_signature is None:
    raise_model_input_error(model)

@def_function.function(input_signature=input_signature)
def _wrapped_model(*args):
    """A concrete tf.function that wraps the model's call function."""
    # When given a single input, Keras models will call the model on the tensor
    # rather than a list consisting of the single tensor.
    inputs = args[0] if len(input_signature) == 1 else list(args)

    with base_layer_utils.call_context().enter(
        model, inputs=inputs, build_graph=False, training=False, saving=True):
        outputs = model(inputs, training=False)

    # Outputs always has to be a flat dict.
    output_names = model.output_names  # Functional Model.
    if output_names is None:  # Subclassed Model.
        from tensorflow.python.keras.engine import compile_utils  # pylint: disable=g-import-not-at-top
        output_names = compile_utils.create_pseudo_output_names(outputs)
    outputs = nest.flatten(outputs)
    exit({name: output for name, output in zip(output_names, outputs)})

exit(_wrapped_model)
