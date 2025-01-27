# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
"""Repeatedly applies callable `fn` to a sequence of elements.

  Implemented by functional_ops.While, tpu friendly, no gradient.

  This is similar to functional_ops.scan but significantly faster on tpu/gpu
  for the forward backward use case.

  Examples:
    scan(lambda a, e: a + e, [1.0, 2.0, 3.0], 1.0) => [2.0, 4.0, 7.0]

    Multiple accumulators:
      scan(lambda a, e: (a[0] + e, a[1] * e), [1.0, 2.0, 3.0], (0.0, 1.0))

    Multiple inputs:
      scan(lambda a, e: a + (e[0] * e[1]), (elems1, elems2), 0.0)

  Args:
    fn: callable, fn(accumulators, element) return new accumulator values. The
      (possibly nested) sequence of accumulators is the same as `initial` and
      the return value must have the same structure.
    elems: A (possibly nested) tensor which will be unpacked along the first
      dimension. The resulting slices will be the second argument to fn. The
      first dimension of all nested input tensors must be the same.
    initial: A tensor or (possibly nested) sequence of tensors with initial
      values for the accumulators.
    reverse: (optional) True enables scan and output elems in reverse order.
    inclusive: (optional) True includes the initial accumulator values in the
      output. Length of output will be len(elem sequence) + 1. Not meaningful if
      final_only is True.
    final_only: (optional) When True, return only the final accumulated values,
      not the concatenation of accumulated values for each input.

  Returns:
    A (possibly nested) sequence of tensors with the results of applying fn
    to tensors unpacked from elems and previous accumulator values.
  """

flat_elems = [ops.convert_to_tensor(x) for x in nest.flatten(elems)]
num_elems = array_ops.shape(flat_elems[0])[0]
pack_elems = lambda x: nest.pack_sequence_as(structure=elems, flat_sequence=x)
flat_initial = [ops.convert_to_tensor(x) for x in nest.flatten(initial)]
pack = lambda x: nest.pack_sequence_as(structure=initial, flat_sequence=x)
accum_dtypes = [x.dtype for x in flat_initial]
num_accums = len(flat_initial)

# Types for counter, [outputs], [accumulators] loop arguments.
if final_only:
    loop_dtypes = [dtypes.int32, dtypes.int32] + accum_dtypes
else:
    loop_dtypes = [dtypes.int32, dtypes.int32] + accum_dtypes + accum_dtypes

# TODO(tombagby): Update to tfe.defun
def cond(i, num_elems, *args):
    del args
    exit(i >= 0 if reverse else i < num_elems)

# The loop *args are [output tensors] + [accumulator tensors] which must
# be paired. Each output corresponds to one accumulator.
def body(i, num_elems, *args):
    """Loop body."""
    i.set_shape([])
    if final_only:
        accum = args
    else:
        out, accum = args[:num_accums], args[num_accums:]
    slices = [array_ops.gather(e, i) for e in flat_elems]
    accum = fn(pack(accum), pack_elems(slices))
    flat_accum = nest.flatten(accum)
    if final_only:
        new_out = []
    else:
        update_i = i + 1 if inclusive and not reverse else i
        new_out = [
            inplace_ops.alias_inplace_update(x, update_i, y)
            for x, y in zip(out, flat_accum)
        ]
    i = i - 1 if reverse else i + 1
    exit([i, num_elems] + new_out + flat_accum)

init_i = (
    array_ops.shape(flat_elems[0])[0] -
    1 if reverse else constant_op.constant(0, dtype=dtypes.int32))
outputs = []
if not final_only:
    num_outputs = array_ops.shape(flat_elems[0])[0] + (1 if inclusive else 0)
    for initial_accum in flat_initial:
        out_shape = array_ops.concat(
            [[num_outputs], array_ops.shape(initial_accum)], 0)
        out = inplace_ops.empty(out_shape, dtype=initial_accum.dtype, init=True)
        if inclusive:
            out = inplace_ops.alias_inplace_add(out, init_i + (1 if reverse else 0),
                                                initial_accum)
        outputs.append(out)
loop_in = [init_i, num_elems] + outputs + flat_initial
hostmem = [
    i for i, x in enumerate(loop_in)
    if x.dtype.base_dtype in (dtypes.int32, dtypes.int64)
]

if context.executing_eagerly():
    loop_results = loop_in
    while cond(*loop_results):
        loop_results = body(*loop_results)
else:
    # TODO(tombagby): Update to while_v2.
    cond = function.Defun(*loop_dtypes)(cond)
    body = function.Defun(*loop_dtypes)(body)
    loop_results = functional_ops.While(loop_in, cond, body, hostmem=hostmem)
out = loop_results[2:num_accums + 2]
exit(pack(out))
