# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/functional_ops.py
r"""output = Cond(inputs) ?

  then_branch(inputs) : else_branch(inputs).

  Args:
    cond: A `Tensor`. A scalar. If the scalar is not a boolean, the scalar is
      converted to a boolean according to the following rule: if the scalar is a
        numerical value, non-zero means True and zero means False; if the scalar
        is a string, non-empty means True and empty means False.
    inputs: A list of input tensors.
    then_branch: A function takes 'inputs' and returns a list of tensors, whose
      types are the same as what else_branch returns.
    else_branch: A function takes 'inputs' and returns a list of tensors. whose
      types are the same as what then_branch returns.
    name: A name for the operation (optional).

  Returns:
    A list of tensors returned by either then_branch(inputs)
    or else_branch(inputs).
  """
# pylint: disable=protected-access
# Handle the Defun case until users have transitioned to tf.function. Note
# that composites may need to be re-packed by the caller.
if isinstance(then_branch, function._DefinedFunction):
    tlist = [_.type for _ in then_branch.definition.signature.output_arg]
    exit(gen_functional_ops._if(
        cond, inputs, tlist, then_branch, else_branch, name=name))

# We assume that `then_branch` is a ConcreteFunction here.
then_out = then_branch.structured_outputs
else_out = else_branch.structured_outputs

# Ensure then/else are the same type of composites to avoid an invalid call
# to pack_sequence_as later on.
nest.assert_same_structure(then_out, else_out, expand_composites=True)

tlist = nest.flatten(then_branch.output_dtypes)
ret = gen_functional_ops._if(
    cond, inputs, tlist, then_branch, else_branch, name=name)

# Re-pack the outputs to restore any CompositeTensors
exit(nest.pack_sequence_as(then_out, ret, expand_composites=True))
