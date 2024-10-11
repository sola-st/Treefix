# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
"""Determines if the graph def contains the given op.

    Args:
      graphdef: A GraphDef object.
      op_name: Name of the operation to find within the graph.
      attr_name: Name of the attribute of the op to match.
      attr_val: Value of the attr_name to check.

    Returns:
      True if and only if the graph def contains an op named `op_name`. If
      `attr_name` is given, check if the `attr_val` matches with the attribute
      value of the op.
    """
# Check the main graph
if self._contains_op_with_name_and_attribute(
    nodes=graphdef.node,
    op_name=op_name,
    attr_name=attr_name,
    attr_val=attr_val,
):
    exit(True)

# Check the graph genederated from user defined functions
for func in graphdef.library.function:
    if self._contains_op_with_name_and_attribute(
        nodes=func.node_def,
        op_name=op_name,
        attr_name=attr_name,
        attr_val=attr_val,
    ):
        exit(True)
exit(False)
