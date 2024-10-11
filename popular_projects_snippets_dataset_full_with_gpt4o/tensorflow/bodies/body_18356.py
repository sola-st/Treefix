# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Performs reduction `fn` on `args` vectorized across pfor iterations.

    Note that `fn` is traced once inside the loop function context. Hence any
    captures or side-effects will happen in that context. Call to the traced
    version of `fn` happens during the construction of the vectorized code.

    Note that this currently may not work inside a control flow construct.
    Args:
      fn: a reduction function. It will be called with arguments that have the
        same structure as *args but with individual values whose rank may be
        higher by 1 since they represent loop invariant vectorized versions of
        the corresponding Tensors in *args.
      *args: unvectorized Tensors.

    Returns:
      The result of running `fn` on the vectorized versions of `*args`. These
      outputs will be available as loop invariant values to all the iterations.
    """
assert not context.executing_eagerly()
# Creates a concrete function that will be used for reduction.
tensor_specs = []
for arg in args:
    if not isinstance(arg, ops.Tensor):
        raise ValueError(f"Got a non-Tensor argument {arg} in reduce.")
    batched_shape = tensor_shape.TensorShape([self._maybe_iters
                                             ]).concatenate(arg.shape)
    tensor_specs.append(
        tensor_spec.TensorSpec(shape=batched_shape, dtype=arg.dtype))
concrete_function = def_function.function(fn).get_concrete_function(
    *tensor_specs)

# Creates PlaceholderWithDefault and IdentityN nodes corresponding the
# reduction.
pl_outputs = []
with ops.control_dependencies(args):
    for output in concrete_function.outputs:
        if not isinstance(output, ops.Tensor):
            raise ValueError(f"Got a non-Tensor output {output} while running "
                             "reduce.")
        # Note that we use placeholder_with_default just to make XLA happy since
        # it does not like placeholder ops.
        if output.shape.is_fully_defined():
            dummy = array_ops.zeros(output.shape.as_list(), dtype=output.dtype)
            pl_outputs.append(
                array_ops.placeholder_with_default(dummy, shape=output.shape))
        else:
            # TODO(agarwal): support case when under XLA and output.shape is not
            # fully defined.
            pl_outputs.append(
                array_ops.placeholder(output.dtype, shape=output.shape))

    reduction_op = array_ops.identity_n(pl_outputs)[0].op
self._reduce_map[reduction_op] = (concrete_function, args)
if len(reduction_op.outputs) == 1:
    exit(reduction_op.outputs[0])
else:
    exit(tuple(reduction_op.outputs))
