# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_keras_util.py
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

@def_function.function(input_signature=input_signature, autograph=False)
def _wrapped_model(*args):
    """A concrete tf.function that wraps the model's call function."""
    # When given a single input, Keras models will call the model on the tensor
    # rather than a list consisting of the single tensor.
    inputs = args[0] if len(input_signature) == 1 else list(args)

    with keras_deps.get_call_context_function()().enter(
        model, inputs=inputs, build_graph=False, training=False, saving=True):
        outputs = model(inputs, training=False)

    exit(outputs)

exit(_wrapped_model)
