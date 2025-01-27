# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
self._pfor_input = pfor_input
self._pfor = pfor_input.pfor
cond_func_name = pfor_input.get_attr("cond").name
self._cond_func = pfor_input.op.graph._get_function(compat.as_bytes(
    cond_func_name))
body_func_name = pfor_input.get_attr("body").name
self._body_func = pfor_input.op.graph._get_function(compat.as_bytes(
    body_func_name))
if self._cond_func is None or self._body_func is None:
    raise ValueError("Error extracting cond and body functions for op "
                     f"{self._pfor_input.op}.")
# Indices of inputs that are passed unchanged through the while loop body.
# Typically these are tensors captured from outside the body context.
self._body_pass_through_indices = set()
for i, (inp, out) in enumerate(zip(self._body_func.graph.inputs,
                                   self._body_func.graph.outputs)):
    if id(inp) == id(out):
        self._body_pass_through_indices.add(i)
self._parallel_iterations = self._pfor_input.get_attr("parallel_iterations")
