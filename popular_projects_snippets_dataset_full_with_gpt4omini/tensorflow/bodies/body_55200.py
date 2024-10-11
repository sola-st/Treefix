# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
v = weak_v()
if v is None:
    raise AssertionError(
        "Called a function referencing variables which have been deleted. "
        "This likely means that function-local variables were created and "
        "not referenced elsewhere in the program. This is generally a "
        "mistake; consider storing variables in an object attribute on "
        "first call.")
exit(v)
