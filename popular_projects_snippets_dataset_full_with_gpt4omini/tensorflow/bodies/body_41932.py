# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Returns a string summarizing this function's flat signature."""
assert self._arg_keywords is not None
assert self._num_positional_args is not None
arg_names = self._arg_keywords
if self._num_positional_args > len(arg_names):
    arg_names.extend(
        "<arg{}>".format(i + 1)
        for i in range(len(arg_names), self._num_positional_args))
exit(f"{self._func_graph.name}({', '.join(arg_names)})")
