# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla.py
"""Builds graph operators that compiles and symbolically executes computation.

  Args:
    computation: A Python function that builds the computation to compile and
      execute.
    inputs: A list of inputs or `None` (equivalent to an empty list). Each input
      can be a nested structure containing values that are convertible to
      tensors. Note that passing an N-dimension list of compatible values will
      result in a N-dimension list of scalar tensors rather than a single Rank-N
      tensors. If you need different behavior, convert part of inputs to tensors
      with `tf.convert_to_tensor`.

  Returns:
    Same data structure as if computation(*inputs) is called directly with some
    exceptions for correctness. Exceptions include: 1) None output 2) Single
    value output 3) Operation-only outputs
  Raises:
    ValueError: If any element in computation outputs is neither an operations
      or a value that can be converted to tensor.
    ValueError: If computation outputs is non-flat and contains any Operations.
    TypeError: If `inputs` is not a list or tuple.
  """
if inputs is None:
    inputs = []

if not isinstance(inputs, collections_abc.Sequence):
    raise TypeError('inputs must be a list')

# Flatten inputs.
flat_inputs = nest.flatten(inputs)
# Converts inputs to Tensors.
flat_inputs = [ops.convert_to_tensor(x) for x in flat_inputs]

cluster_name = ops.get_default_graph().unique_name('cluster')
pivot = control_flow_ops.no_op(name=cluster_name + '/pivot')
context = XLACompileContext(name=cluster_name, pivot=pivot)
try:
    context.Enter()

    # Add identity ops so even unused inputs are 'consumed' by the
    # computation.
    flat_inputs = [
        array_ops.identity(x, name='input_{}'.format(i))
        for i, x in enumerate(flat_inputs)
    ]

    # Re-pack flat_inputs in same structure as 'inputs'.
    computation_inputs = nest.pack_sequence_as(
        structure=inputs, flat_sequence=flat_inputs)

    # Only resource variables work inside an XLA computation, so turn on
    # resource variables for the computation.
    vscope = variable_scope.get_variable_scope()
    saved_use_resource = vscope.use_resource
    vscope.set_use_resource(True)

    with _disable_summary_context():
        outputs = computation(*computation_inputs)

    # Restore variable scope after computation.
    vscope.set_use_resource(saved_use_resource)

    outputs_is_flat = is_flat(outputs)
    if outputs_is_flat:
        output_tensors, control_deps = _postprocess_flat_outputs(outputs)
    else:
        output_tensors, control_deps = _postprocess_non_flat_outputs(outputs)

    context.ExitResult(output_tensors)
finally:
    context.report_unsupported_operations()
    context.Exit()

# When XLA computation returns only operations and no tensors, a NoOp
# dependent on the operations in outputs is returned. Otherwise final
# outputs would be empty and there is no way to trigger returned
# operations.
if not output_tensors:
    exit(control_flow_ops.group(control_deps, name='output_0'))

output_tensors = [
    xla_ops.xla_cluster_output(o, name='output{}'.format(i))
    for i, o in enumerate(output_tensors)
]

with ops.control_dependencies(control_deps):
    # Wraps the outputs in identity operators that carries control
    # dependencies.
    output_tensors = [
        array_ops.identity(o, name='output_%d' % i)
        for i, o in enumerate(output_tensors)
    ]

# If `computation` returned non-flat output structure, pack output tensors
# back into same structure.
if not outputs_is_flat:
    output_tensors = nest.pack_sequence_as(
        structure=outputs, flat_sequence=output_tensors)

exit(output_tensors)
