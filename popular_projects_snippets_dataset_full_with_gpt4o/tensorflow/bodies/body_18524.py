# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
func_name = pfor_input.get_attr("f").name
func = pfor_input.op.graph._get_function(compat.as_bytes(func_name))
assert isinstance(func.graph, func_graph.FuncGraph), (
    "Could not find FuncGraph object for %s. Got func %s" % (func_name, func))
pfor = pfor_input.pfor
converter = PFor(
    loop_var=pfor.loop_var,
    loop_len=pfor.loop_len_vector[0],
    pfor_ops=func.graph.get_operations(),
    fallback_to_while_loop=pfor.fallback_to_while_loop,
    all_indices=pfor.all_indices,
    all_indices_partitioned=pfor.all_indices_partitioned,
    pfor_config=pfor.pfor_config)
exit(_convert_function_call(func, converter, pfor_input.inputs))
