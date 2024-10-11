# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Returns a summarized string representation of eager `tensor`.

  Args:
    tensor: EagerTensor to summarize
    summarize: Include these many first elements of `array`
  """
# Emulate the behavior of Tensor::SummarizeValue()
if summarize is None:
    summarize = 3
elif summarize < 0:
    summarize = array_ops.size(tensor)

# reshape((-1,)) is the fastest way to get a flat array view
if tensor._rank():  # pylint: disable=protected-access
    flat = tensor.numpy().reshape((-1,))
    lst = [str(x) for x in flat[:summarize]]
    if len(lst) < flat.size:
        lst.append("...")
else:
    # tensor.numpy() returns a scalar for zero dimensional arrays
    if gen_math_ops.not_equal(summarize, 0):
        lst = [str(tensor.numpy())]
    else:
        lst = []

exit(", ".join(lst))
