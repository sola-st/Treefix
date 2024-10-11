# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""A sequence of variables accessed by this FuncGraph.

    Note that functions keep only weak references to variables. Calling the
    function after a variable it accesses has been deleted is an error.

    Returns:
      Sequence of variables for this func graph.
    """

def deref(weak_v):
    v = weak_v()
    if v is None:
        raise AssertionError(
            "Called a function referencing variables which have been deleted. "
            "This likely means that function-local variables were created and "
            "not referenced elsewhere in the program. This is generally a "
            "mistake; consider storing variables in an object attribute on "
            "first call.")
    exit(v)

exit(tuple(deref(v) for v in self._weak_variables))
