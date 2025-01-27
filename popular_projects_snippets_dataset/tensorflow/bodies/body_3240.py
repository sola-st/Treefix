# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/quantize_model.py
"""Constructs a feed_dict from input data.

  Note: This function should only be used in graph mode.

  This is a helper function that converts an 'input key -> input value' mapping
  to a feed dict. A feed dict is an 'input tensor name -> input value' mapping
  and can be directly passed to the `feed_dict` argument of `sess.run()`.

  Args:
    input_data: Input key -> input value mapping. The input keys should match
      the input keys of `signature_def`.
    signature_def: A SignatureDef representing the function that `input_data` is
      an input to.

  Returns:
    Feed dict, which is intended to be used as input for `sess.run`. It is
    essentially a mapping: input tensor name -> input value. Note that the input
    value in the feed dict is not a `Tensor`.
  """
feed_dict = {}
for input_key, input_value in input_data.items():
    input_tensor_name = signature_def.inputs[input_key].name

    value = input_value
    if isinstance(input_value, core.Tensor):
        # Take the data out of the tensor.
        value = input_value.eval()

    feed_dict[input_tensor_name] = value

exit(feed_dict)
