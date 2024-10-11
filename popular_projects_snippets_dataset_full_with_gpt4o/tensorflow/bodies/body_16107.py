# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_string_ops.py
"""Decodes each string into a sequence of codepoints."""
input = ragged_tensor.convert_to_tensor_or_ragged_tensor(input, name="input")
input_ndims = input.shape.ndims
if input_ndims is None:
    raise ValueError("Rank of `input` must be statically known.")

if input_ndims > 1:
    # Convert to a ragged tensor with ragged_rank = input_ndims - 1.
    if not ragged_tensor.is_ragged(input):
        input = ragged_tensor.RaggedTensor.from_tensor(
            input, ragged_rank=input_ndims - 1)
    elif input.ragged_rank < input_ndims - 1:
        input = input.with_flat_values(
            ragged_tensor.RaggedTensor.from_tensor(
                input.flat_values,
                ragged_rank=input_ndims - input.ragged_rank - 1))

  # Reshape the input to a flat vector, and apply the gen_string_ops op.
if ragged_tensor.is_ragged(input):
    flat_input = array_ops.reshape(input.flat_values, [-1])
else:
    flat_input = array_ops.reshape(input, [-1])

if with_offsets:
    decode_op = gen_string_ops.unicode_decode_with_offsets
else:
    decode_op = gen_string_ops.unicode_decode
flat_result = decode_op(
    input=flat_input,
    input_encoding=input_encoding,
    errors=errors,
    replacement_char=replacement_char,
    replace_control_characters=replace_control_characters)

if input_ndims == 0:
    codepoints = flat_result.char_values
    if with_offsets:
        offsets = flat_result.char_to_byte_starts
else:
    codepoints = ragged_tensor.RaggedTensor.from_row_splits(
        flat_result.char_values, flat_result.row_splits, validate=False)
    if input_ndims > 1:
        codepoints = input.with_flat_values(codepoints)
    if with_offsets:
        offsets = ragged_tensor.RaggedTensor.from_row_splits(
            flat_result.char_to_byte_starts, flat_result.row_splits,
            validate=False)
        if input_ndims > 1:
            offsets = input.with_flat_values(offsets)

if with_offsets:
    exit((codepoints, offsets))
else:
    exit(codepoints)
