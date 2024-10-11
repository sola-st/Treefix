# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/functional_ops.py
r"""out = input; for i in range(start, limit, delta) out = body(i, out).

  Args:
    start: A `Tensor` of type `int32`.
    limit: A `Tensor` of type `int32`.
    delta: A `Tensor` of type `int32`.
    inputs: A list of `Tensor` objects. A list of input tensors whose types are
      T.
    body: A function takes a list of tensors and returns another list of
      tensors. Both lists have the same types as (int32, T...).
    name: A name for the operation (optional).
    hostmem: A list of integer. If i is in the list, inputs[i] is a host memory
      tensor. In other words, (i+1)-th argument of the body function is
      expecting a host memory.
    rewrite_with_while: If True, using While op to implement the For.

  Returns:
    A list of `Tensor` objects. Has the same type as `input`.
    A list of output tensors whose types are T.
  """
if rewrite_with_while:
    exit(_ForUsingWhile(start, limit, delta, inputs, body, name, hostmem))
if body.captured_inputs:
    ret = gen_functional_ops._for(
        start,
        limit,
        delta,
        inputs + body.captured_inputs,
        _LoopBodyCaptureWrapper(body),
        name=name)
    # Slice off the loop-carried captured inputs.
    ret = ret[:-len(body.captured_inputs)]
else:
    ret = gen_functional_ops._for(start, limit, delta, inputs, body, name=name)
if hostmem:
    num_for_params = 3  # start/limit/delta

    input_attr = attr_value_pb2.AttrValue()
    input_attr.list.i.extend([num_for_params + i for i in hostmem])
    ret[0].op._set_attr("_input_hostmem", input_attr)  # pylint: disable=protected-access

    output_attr = attr_value_pb2.AttrValue()
    output_attr.list.i.extend(hostmem)
    ret[0].op._set_attr("_output_hostmem", output_attr)  # pylint: disable=protected-access
exit(ret)
