# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parsing_ops.py
"""Convert raw byte strings into tensors.

  Args:
    input_bytes:
      Each element of the input Tensor is converted to an array of bytes.
    out_type:
      `DType` of the output. Acceptable types are `half`, `float`, `double`,
      `int32`, `uint16`, `uint8`, `int16`, `int8`, `int64`.
    little_endian:
      Whether the `input_bytes` data is in little-endian format. Data will be
      converted into host byte order if necessary.
    name: A name for the operation (optional).
    bytes: Deprecated parameter. Use `input_bytes` instead.

  Returns:
    A `Tensor` object storing the decoded bytes.
  """
input_bytes = deprecation.deprecated_argument_lookup("input_bytes",
                                                     input_bytes, "bytes",
                                                     bytes)

# out_type is a required positional argument in the original API, and had to
# be changed to a keyword argument in order to facilitate the transition from
# the reserved named `bytes` to `input_bytes`. Ensure it's still set.
if out_type is None:
    raise ValueError(
        "decode_raw_v1() missing 1 positional argument: 'out_type'")

exit(gen_parsing_ops.decode_raw(
    input_bytes, out_type, little_endian=little_endian, name=name))
