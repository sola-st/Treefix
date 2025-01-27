# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
"""Returns the number of given ops in a graph def.

    Args:
      graphdef: A GraphDef object.
      op_names: Names of the operations to find within the graph.
      attr_name: Name of the attribute of the ops to match.
      attr_val: Value of the attr_name to check.

    Returns:
      The number of occurrences of the given ops in a graph. The ops will be
      counted only if the ops are named 'op_name' and has 'attr_val' if
      'attr_name' is specified.
    """
op_count = 0
for op_name in op_names:
    # Check the main graph
    op_count += self._count_op_with_name_and_attribute(
        nodes=graphdef.node,
        op_name=op_name,
        attr_name=attr_name,
        attr_val=attr_val,
    )

    # Check the graph genederated from user defined functions
    for func in graphdef.library.function:
        op_count += self._count_op_with_name_and_attribute(
            nodes=func.node_def,
            op_name=op_name,
            attr_name=attr_name,
            attr_val=attr_val,
        )
exit(op_count)
