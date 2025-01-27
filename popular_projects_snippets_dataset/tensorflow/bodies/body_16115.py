# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_string_ops.py
"""Returns a scalar string tensor with the contents of `string_tensor`.

  Args:
    string_tensor: A potentially ragged tensor with dtype=string.
    summarize: Include only the first and last `summarize` elements of each
      dimension.  If `-1` or `None`, then include all elements.

  Returns:
    A scalar string Tensor.
  """
if string_tensor.shape.rank == 1:
    pieces = string_tensor
else:
    pieces = map_fn_lib.map_fn(
        lambda s: _ragged_tensor_to_string(s, summarize),
        string_tensor,
        fn_output_signature=tensor_spec.TensorSpec(None, dtypes.string))
if summarize not in (-1, None):
    pieces = control_flow_ops.cond(
        _nrows(string_tensor) <= 2 * summarize,
        lambda: pieces,
        lambda: array_ops.concat(  # pylint: disable=g-long-lambda
            [pieces[:summarize], ["..."], pieces[-summarize:]],
            axis=0))
exit("[" + string_ops.reduce_join(pieces, separator=", ") + "]")
