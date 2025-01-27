# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
"""Add node(s) to graph representing output operands and returns type.

    Args:
      fused_op_name: name of the fused op stub name.
      output_index: Output index that we are currently processing from stub.
      out_graphdef: The destination graphdef we are currently building up.

    Returns:
      The datatype of this identity.

    Raises:
      RuntimeError: if the method is not implemented.
    """
del fused_op_name, output_index, out_graphdef
raise RuntimeError("Unimplemented abstract method.")
