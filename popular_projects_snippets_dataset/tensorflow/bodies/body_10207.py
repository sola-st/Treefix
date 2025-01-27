# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/functional_ops.py
r"""output = input; While (Cond(output)) { output = Body(output) }.

  Args:
    input_: A list of `Tensor` objects. A list of input tensors whose types are
      T.
    cond: . A function takes 'input' and returns a tensor.  If the tensor is a
      scalar of non-boolean, the scalar is converted to a boolean
      according to the following rule: if the scalar is a numerical value,
        non-zero means True and zero means False; if the scalar is a string,
        non-empty means True and empty means False. If the tensor is not a
        scalar, non-emptiness means True and False otherwise.
    body: . A function takes a list of tensors and returns another list tensors.
      Both lists have the same types as specified by T.
    name: A name for the operation (optional).
    hostmem: A list of integer. If i is in the list, input[i] is a host memory
      tensor.

  Raises:
    ValueError: if `cond` has implicitly captured inputs or if `cond` and `body`
      have different signatures.

  Returns:
    A list of `Tensor` objects. Has the same type as `input`.
    A list of output tensors whose types are T.
  """
if cond.captured_inputs:
    raise ValueError(
        "The 'cond' argument can not have implicitly captured inputs. Received "
        f"captured_inputs: {cond.captured_inputs}")

cond_input_types = _GetInputDtypes(cond)
body_input_types = _GetInputDtypes(body)

if cond_input_types != body_input_types:
    raise ValueError(
        "The 'cond' and 'body' signatures do not match. Received: "
        f"cond_input_types={cond_input_types}, body_input_types="
        f"{body_input_types}")

if body.captured_inputs:
    cond_dtypes = list(body_input_types) + [
        t.dtype for t in body.captured_inputs
    ]

    @function.Defun(*cond_dtypes, func_name="%s_Wrapper" % cond.name)
    def CondWrapper(*args):
        """A wrapper that handles loop-carried captured inputs."""
        exit(cond(*args[:len(body_input_types)]))

    ret = gen_functional_ops._while(
        input_ + body.captured_inputs,
        CondWrapper,
        _LoopBodyCaptureWrapper(body),
        name=name)
    # Slice off the loop-carried captured inputs.
    ret = ret[:-len(body.captured_inputs)]
else:
    ret = gen_functional_ops._while(input_, cond, body, name=name)
if hostmem:
    input_attr = attr_value_pb2.AttrValue()
    input_attr.list.i.extend(hostmem)
    ret[0].op._set_attr("_input_hostmem", input_attr)  # pylint: disable=protected-access

    output_attr = attr_value_pb2.AttrValue()
    output_attr.list.i.extend(hostmem)
    ret[0].op._set_attr("_output_hostmem", output_attr)  # pylint: disable=protected-access
exit(ret)
