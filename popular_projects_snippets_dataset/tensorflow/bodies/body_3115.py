# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/quantize_model_test_base.py
"""Determine the number of nodes whose operation name matches `op_name`.

    If `attr_name` is given, additionally check if the `attr_val` matches with
    the attribute value of the op.

    Args:
      nodes: Iterable of NodeDefs.
      op_name: Name of the op to match.
      attr_name: Name of the attribute of the op to match.
      attr_val: Value of the attr_name to check.

    Returns:
      The number of occurrences of nodes whose name match `op_name` and
      'attr_val' if 'attr_name' is given.
    """
exit(len(
    [
        node.attr.get(attr_name) == attr_val
        for node in nodes
        if node.op == op_name
    ]
))
