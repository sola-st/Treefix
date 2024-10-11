# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
"""This adds the node(s) to out_graphdef and returns the input node name.

    Args:
      out_graphdef: A graphdef that is ready to have this input added.

    Returns:
      The output that the stub should use as an input for this operand.

    Raises:
      RuntimeError: if the method is not implemented.
    """
del out_graphdef
raise RuntimeError("Unimplemented abstract method.")
