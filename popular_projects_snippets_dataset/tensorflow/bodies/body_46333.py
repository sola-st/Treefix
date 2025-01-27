# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/type_inference.py
"""Resolves the type of a (possibly annotated) function argument.

    Args:
      ns: namespace
      types_ns: types namespace
      f_name: str, the function name
      name: str, the argument name
      type_anno: the type annotating the argument, if any
      f_is_local: bool, whether the function is a local function
    Returns:
      Set of the argument types.
    """
raise NotImplementedError('subclasses must implement')
