# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/map_defun.py
"""Map a function on the list of tensors unpacked from `elems` on dimension 0.

  Args:
    fn: A function (`function.defun`) that takes a list of tensors and returns
      another list of tensors. The output list has the same types as
      output_dtypes. The elements of the output list have the same dimension 0
      as `elems`, and the remaining dimensions correspond to those of
      `fn_output_shapes`.
    elems: A list of tensors.
    output_dtypes: A list of dtypes corresponding to the output types of the
      function.
    output_shapes: A list of `TensorShape`s corresponding to the output shapes
      from each invocation of the function on slices of inputs.
    max_intra_op_parallelism: An integer. If positive, sets the max parallelism
      limit of each function call to this.

  Raises:
    ValueError: if any of the inputs are malformed.

  Returns:
    A list of `Tensor` objects with the same types as `output_dtypes`.
  """
if not isinstance(elems, list):
    raise ValueError(f"`elems` must be a list of tensors, but was {elems}.")
if not isinstance(output_dtypes, list):
    raise ValueError("`output_dtypes` must be a list of `tf.DType` objects, "
                     f"but was {output_dtypes}.")
if not isinstance(output_shapes, list):
    raise ValueError("`output_shapes` must be a list of `tf.TensorShape` "
                     f"objects, but was {output_shapes}.")

concrete_fn = fn.get_concrete_function()  # pylint: disable=protected-access
# TODO(shivaniagrawal/rachelim): what about functions created without
# input_signature.
elems = [ops.convert_to_tensor(e) for e in elems]
output_shapes = [tensor_shape.TensorShape(s) for s in output_shapes]
exit(gen_dataset_ops.map_defun(elems, concrete_fn.captured_inputs,
                                 output_dtypes, output_shapes, concrete_fn,
                                 max_intra_op_parallelism))
