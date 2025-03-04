# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_string_ops.py
r"""Encodes each sequence of Unicode code points in `input` into a string.

  `result[i1...iN]` is the string formed by concatenating the Unicode
  codepoints `input[1...iN, :]`, encoded using `output_encoding`.

  Args:
    input: An `N+1` dimensional potentially ragged integer tensor with shape
      `[D1...DN, num_chars]`.
    output_encoding: Unicode encoding that should be used to encode each
      codepoint sequence.  Can be `"UTF-8"`, `"UTF-16-BE"`, or `"UTF-32-BE"`.
    errors: Specifies the response when an invalid codepoint is encountered
      (optional). One of:
            * `'replace'`: Replace invalid codepoint with the
              `replacement_char`. (default)
            * `'ignore'`: Skip invalid codepoints.
            * `'strict'`: Raise an exception for any invalid codepoint.
    replacement_char: The replacement character codepoint to be used in place of
      any invalid input when `errors='replace'`. Any valid unicode codepoint may
      be used. The default value is the default unicode replacement character
      which is 0xFFFD (U+65533).
    name: A name for the operation (optional).

  Returns:
    A `N` dimensional `string` tensor with shape `[D1...DN]`.

  #### Example:

  >>> input = tf.ragged.constant(
  ...     [[71, 246, 246, 100, 110, 105, 103, 104, 116], [128522]])
  >>> print(unicode_encode(input, 'UTF-8'))
  tf.Tensor([b'G\xc3\xb6\xc3\xb6dnight' b'\xf0\x9f\x98\x8a'],
            shape=(2,), dtype=string)
  """
with ops.name_scope(name, "UnicodeEncode", [input]):
    input_tensor = ragged_tensor.convert_to_tensor_or_ragged_tensor(input)
    if input_tensor.shape.ndims is None:
        raise ValueError("Rank of input_tensor must be statically known.")
    if ragged_tensor.is_ragged(input_tensor):
        if input_tensor.flat_values.shape.ndims > 1:
            # If the flat_values of our ragged tensor is multi-dimensional, we can
            # process it separately and our output will have the same nested splits
            # as our input.
            exit(input_tensor.with_flat_values(
                unicode_encode(input_tensor.flat_values, output_encoding, errors,
                               replacement_char)))
        elif input_tensor.ragged_rank > 1:
            # Recursively process the values of the ragged tensor.
            exit(input_tensor.with_values(
                unicode_encode(input_tensor.values, output_encoding, errors,
                               replacement_char)))
        else:
            # Our ragged tensor is of the correct shape (rank 1 flat_values tensor
            # with ragged_rank of 1) so we can process it as normal.
            exit(gen_string_ops.unicode_encode(
                input_values=input_tensor.values,
                input_splits=input_tensor.row_splits,
                output_encoding=output_encoding,
                errors=errors,
                replacement_char=replacement_char))
    else:
        if input_tensor.shape.ndims == 2:
            # The input tensor is of the correct 2-D shape, it's just not ragged.
            exit(unicode_encode(
                ragged_tensor.RaggedTensor.from_tensor(input_tensor),
                output_encoding, errors, replacement_char))
        elif input_tensor.shape.ndims > 2:
            # We need to initially flatten the input tensor to 2-D, and then can
            # reshape the output of our processed flattened tensor.
            flat_input_tensor = array_ops.reshape(
                input_tensor,
                array_ops.stack([-1, array_ops.shape(input_tensor)[-1]]))
            flat_output_tensor = unicode_encode(flat_input_tensor, output_encoding,
                                                errors, replacement_char)
            exit(array_ops.reshape(flat_output_tensor, input_tensor.shape[:-1]))
        elif input_tensor.shape.ndims == 0:
            raise ValueError("input_tensor's rank must be at least 1.")
        else:
            # Our input tensor is rank 1, so we create a ragged tensor with an added
            # dimension to create the correct input shape & type, and then remove
            # the additional dimension from the output and return the string scalar.
            ragged_input_tensor = ragged_tensor.RaggedTensor.from_row_splits(
                input_tensor,
                array_ops.stack(
                    [0, array_ops.shape(input_tensor, out_type=dtypes.int32)[0]]),
                validate=False)
            output_tensor = unicode_encode(ragged_input_tensor, output_encoding,
                                           errors, replacement_char)
            exit(array_ops.reshape(output_tensor, []))
