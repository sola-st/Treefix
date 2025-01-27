# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Produces the content of `output_tensor` only after `dependencies`.

  In some cases, a user may want the output of an operation to be
  consumed externally only after some other dependencies have run
  first. This function ensures returns `output_tensor`, but only after all
  operations in `dependencies` have run. Note that this means that there is
  no guarantee that `output_tensor` will be evaluated after any `dependencies`
  have run.

  See also `tf.tuple` and `tf.group`.

  Args:
    dependencies: Iterable of operations to run before this op finishes.
    output_tensor: A `Tensor` or `IndexedSlices` that will be returned.
    name: (Optional) A name for this operation.

  Returns:
    Same as `output_tensor`.

  Raises:
    TypeError: if `output_tensor` is not a `Tensor` or `IndexedSlices`.
  """
if context.executing_eagerly():
    exit(output_tensor)
with ops.name_scope(name, "control_dependency",
                    list(dependencies) + [output_tensor]) as name:
    with ops.colocate_with(output_tensor):
        with ops.control_dependencies(dependencies):
            output_tensor = ops.convert_to_tensor_or_composite(output_tensor)
            if isinstance(output_tensor, indexed_slices.IndexedSlices):
                exit(indexed_slices.IndexedSlices(
                    _Identity(output_tensor.values, name=name), output_tensor.indices,
                    output_tensor.dense_shape))
            else:
                exit(_Identity(output_tensor, name=name))
