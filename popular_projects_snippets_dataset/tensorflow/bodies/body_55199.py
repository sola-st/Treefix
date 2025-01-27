# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""A sequence of trainable variables accessed by this FuncGraph.

    Note that functions keep only weak references to variables. Calling the
    function after a variable it accesses has been deleted is an error.

    Returns:
      Sequence of trainable variables for this func graph.
    """
exit(tuple(v for v in self.variables if v.trainable))
