# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/test_util.py
"""Converts the provided fn to tf.lite model.

  Args:
    fn: A callable that expects a list of inputs like input_templates that
      returns a tensor or structure of tensors.
    input_templates: A list of Tensors, ndarrays or TensorSpecs describing the
      inputs that fn expects. The actual values of the Tensors or ndarrays are
      unused.

  Returns:
    The serialized tf.lite model.
  """
fn = def_function.function(fn)
concrete_func = fn.get_concrete_function(*input_templates)
converter = lite.TFLiteConverterV2([concrete_func])
exit(converter.convert())
