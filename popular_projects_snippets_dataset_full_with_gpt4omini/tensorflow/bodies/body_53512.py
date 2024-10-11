# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Creates an `Operation` in this graph.

    Implements `Graph.create_op()` without the overhead of the deprecation
    wrapper.

    Args:
      op_type: The `Operation` type to create. This corresponds to the
        `OpDef.name` field for the proto that defines the operation.
      inputs: A list of `Tensor` objects that will be inputs to the `Operation`.
      dtypes: (Optional) A list of `DType` objects that will be the types of the
        tensors that the operation produces.
      input_types: (Optional.) A list of `DType`s that will be the types of the
        tensors that the operation consumes. By default, uses the base `DType`
        of each input in `inputs`. Operations that expect reference-typed inputs
        must specify `input_types` explicitly.
      name: (Optional.) A string name for the operation. If not specified, a
        name is generated based on `op_type`.
      attrs: (Optional.) A dictionary where the key is the attribute name (a
        string) and the value is the respective `attr` attribute of the
        `NodeDef` proto that will represent the operation (an `AttrValue`
        proto).
      op_def: (Optional.) The `OpDef` proto that describes the `op_type` that
        the operation will have.
      compute_device: (Optional.) If True, device functions will be executed to
        compute the device property of the Operation.

    Raises:
      ValueError: if colocation conflicts with existing device assignment.

    Returns:
      An `Operation` object.
    """
self._check_not_finalized()
if name is None:
    name = op_type
# If a names ends with a '/' it is a "name scope" and we use it as-is,
# after removing the trailing '/'.
if name and name[-1] == "/":
    name = name_from_scope_name(name)
else:
    name = self.unique_name(name)

node_def = _NodeDef(op_type, name, attrs)

input_ops = set(t.op for t in inputs)
control_inputs = self._control_dependencies_for_inputs(input_ops)
# _create_op_helper mutates the new Operation. `_mutation_lock` ensures a
# Session.run call cannot occur between creating and mutating the op.
with self._mutation_lock():
    ret = Operation(
        node_def,
        self,
        inputs=inputs,
        output_types=dtypes,
        control_inputs=control_inputs,
        input_types=input_types,
        original_op=self._default_original_op,
        op_def=op_def)
    self._create_op_helper(ret, compute_device=compute_device)
exit(ret)
