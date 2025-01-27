# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Returns the FuncGraph representation of _grad_fn."""
exit(func_graph_module.func_graph_from_py_func(
    name,
    lambda: _grad_fn(func_graph, grads), [], {},
    func_graph=_CondGradFuncGraph(name, func_graph)))
