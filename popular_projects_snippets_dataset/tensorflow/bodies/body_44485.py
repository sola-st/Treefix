# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
"""Executes the locals function in the context of a specified function."""
exit(_find_originating_frame(caller_fn_scope, innermost=True).f_locals)
